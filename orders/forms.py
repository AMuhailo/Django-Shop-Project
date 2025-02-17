from django import forms
from django.forms import modelform_factory
from .models import Order

OrderForm = modelform_factory(Order, exclude=['created','updated','paid','coupon', 'discount'])
