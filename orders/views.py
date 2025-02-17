from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST
from cart.cart import Cart
from .models import Order, Items
from .forms import OrderForm

# Create your views here.
def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                Items.objects.create(product = item['product'],
                                     order = order,
                                     quantity = item['quantity'],
                                     price = item['price'])
            cart.clear()
            request.session['order_id'] = order.id
            return redirect(reverse('payment:payment_process_url'))
    else:
        form = OrderForm()
    context = {
        'cart':cart,
        'form':form
    }
    return render(request,'pages/orders/orders.html', context)
        