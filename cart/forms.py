from django import forms
from shop.models import Product

CHOICES_QUANTITY = [(quantity,str(quantity)) for quantity in range(1,11)]

class QuantityForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=CHOICES_QUANTITY, coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
    