from celery import shared_task,Celery
from celery.schedules import crontab
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from .models import Order
app = Celery('myshop')


@shared_task
def send_order(order_id):
    order = get_object_or_404(Order, id=order_id)
    subject = f"Order {order.id}"
    message = f"You order number a {order.id}"
    mail = send_mail(subject, message, 'admin@gmail.com',[order.email])
    return mail
