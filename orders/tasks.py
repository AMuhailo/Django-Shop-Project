from celery import shared_task,Celery
from celery.schedules import crontab
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from .models import Order
app = Celery('myshop')


@shared_task
def send_order(order_id):
    try:  
        order = get_object_or_404(Order, id=order_id)
    except Order.DoesNotExist:
        print(f"Order with ID {order_id} not found. Retrying in 10 seconds...")
        send_order.apply_async(args=[order_id], countdown=10)  # Повтор через 10 секунд
        return None
    subject = f"Order {order.id}"
    message = f"You order number a {order.id}"
    mail = send_mail(subject, message, 'admin@gmail.com',[order.email])
    return mail
