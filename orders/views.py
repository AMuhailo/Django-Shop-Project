from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from cart.cart import Cart
from .models import Order, Items
from .forms import OrderForm
from .tasks import send_order

# Create your views here.
def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                Items.objects.create(product = item['product'],
                                     order = order,
                                     quantity = item['quantity'],
                                     price = item['price'])
            cart.clear()
            send_order.delay_on_commit(order.id)
            return redirect('shop:product_list_url')
    else:
        form = OrderForm()
    context = {
        'cart':cart,
        'form':form
    }
    return render(request,'pages/orders/orders.html', context)
        