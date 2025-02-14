from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.conf import settings
import stripe
from cart.cart import Cart
from orders.models import Order,Items
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_VERSION

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order,id=order_id)
    if request.method == 'POST':
        success_url = request.build_absolute_uri(reverse('payment:success_url'))
        cancel_url = request.build_absolute_uri(reverse('payment:cancel_url'))
        session_data = {
            'mode':'payment',
            'client_reference_id':order.id,
            'success_url':success_url,
            'cancel_url':cancel_url,
            'line_items':[]
        }
        
        for item in order.items_order.all():
            session_data['line_items'].append({
                'price_data':{
                    'unit_amount':int(item.price * Decimal('100')),
                    'currency':'usd',
                    'product_data':{
                        'name':item.product.title,
                    },
                },
                'quantity':item.quantity,
            })
        session = stripe.checkout.Session.create(**session_data)
        return redirect(session.url, code=303)
    else:
        return render(request,'pages/orders/include/placeorder.html',locals())

def success(request):
    return render(request, 'pages/orders/include/success_url.html')

def cancel(request):
    return render(request, 'pages/orders/include/cancel_url.html')