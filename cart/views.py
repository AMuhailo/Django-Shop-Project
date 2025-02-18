from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from coupons.forms import CouponForm
from shop.models import Product
from .cart import Cart
from .forms import QuantityForm

# Create your views here.
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = Product.objects.select_related('category')
    product = get_object_or_404(product,
                                id = product_id)
    form = QuantityForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product,quantity=cd['quantity'],override_quantity = cd['override'])
    return redirect('cart:carts_url')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = Product.objects.select_related('category')
    product = get_object_or_404(product,
                                id = product_id)
    cart.remove(product)
    return redirect('cart:carts_url')

def carts(request):
    cart = Cart(request)
    coupon_form = CouponForm()
    for item in cart:
        item['item_override'] = QuantityForm(initial={'quantity':item['quantity'],
                                                      'override':True})
    context = {
        'cart':cart,
        'coupon_form':coupon_form
    }
    return render(request, 'pages/include/cart_info.html', context)