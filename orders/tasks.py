from django.shortcuts import get_object_or_404
from celery import shared_task
from django.core.mail import send_mail

from orders.models import Order
@shared_task
def order_sender(order_id):
    order = get_object_or_404(Order, id = order_id)
    sender = f"You orders number {order.id}"
    message = f"Orders done {order.id}"
    mail = send_mail(sender, message,'admin@gmail.com', [order.email])
    return mail