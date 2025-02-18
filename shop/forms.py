from django import forms
from django.forms import modelform_factory
from .models import Category, Product

ProductCreateFormset = modelform_factory(model = Product, 
                                   exclude = ['slug','active','created','updated','discount'])


class SearchForm(forms.Form):
    query = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'search...'}))
