from django import forms
from django.forms import modelform_factory
from .models import Category, Product

ProductCreateFormset = modelform_factory(model = Product, 
                                   exclude = ['slug','active','created','updated','discount'],
                                   widgets={
                                       'category':forms.Select(attrs={
                                           'class':'form-select',
                                           'id':'floatingSelect',
                                       }),
                                       'image':forms.FileInput(attrs={
                                           'class':'form-control',
                                           'id':'inputGroupFile01'
                                       }),
                                        'title':forms.TextInput(attrs={
                                            "class":"form-control",
                                            'placeholder':'Title product...',
                                        }),
                                        'description':forms.Textarea(attrs={
                                            'class':'form-control',
                                            'placeholder':'Description product'
                                        }),
                                        'price':forms.NumberInput(attrs={
                                            'class':'form-control',
                                            'value':'0'
                                        }) 
                                   })


class SearchForm(forms.Form):
    query = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control",
                                                                          'placeholder':'search...',
                                                                          "aria-describedby":"button-addon1"}))
