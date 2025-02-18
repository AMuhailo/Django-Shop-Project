from django.shortcuts import get_object_or_404
from celery import shared_task
import subprocess
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from orders.models import Order
@shared_task
def order_sender(order_id):
    order = get_object_or_404(Order, id = order_id)
    sender = f"You orders №{order.id}"
    html_message = render_to_string('pages/orders/emailorder.html', {"order":order})
    message = f"Thank you for your order #{order.id}. Total: ${order.get_total_money}"
    mail = EmailMultiAlternatives(sender, message,'admin@gmail.com', [order.email])
    mail.attach_alternative(html_message,'text/html')
    mail.send()
    return f"Email sent to {order.email}"

@shared_task
def dump_shop():
    try:
        subprocess.run(
            ['python','manage.py','dumpdata', 'shop','--indent=2','--output=shop/fixtures/shop_data.json'],
            check = True
        )
        return f"Dumpdata was success instal!"
    except subprocess.CalledProcessError as error:
        return f"Error in dumpdata {error}"