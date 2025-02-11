from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from shop.models import Product
from .cart import Cart
from .forms import QuantityForm

# Create your views here.
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,
                                id = product_id)
    form = QuantityForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product,quantity=cd['quantity'],override_quantity = cd['override'])
    return redirect('csrt:carts_url')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,
                                id = product_id)
    cart.remove(product)
    return redirect('cart:carts_url')

def carts(request):
    cart = Cart(request)
    context = {
        'cart':cart
    }
    return render(request, 'pages/include/cart_info.html', context)