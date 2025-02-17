from django import forms
from django.forms import modelform_factory
from .models import Category, Product

ProductCreateFormset = modelform_factory(model = Product, 
                                   exclude = ['slug','active','created','updated','discount'])
