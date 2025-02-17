from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
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
            if order.coupon:
                stripe_coupon = stripe.Coupon.create(name = order.coupon.code, percent_off = order.discount, duration = 'once')
                session_data['discounts'] = [{
                    'coupon':stripe_coupon.id
                }]
                session = stripe.checkout.Session.create(**session_data)
                return redirect(session.url, code=303)
    
    else:
        return render(request,'pages/orders/include/placeorder.html',locals())

def success(request):
    return render(request, 'pages/orders/include/success_url.html')

def cancel(request):
    return render(request, 'pages/orders/include/cancel_url.html')


@require_POST
@csrf_exempt
def stripe_webhook(request):
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
    payload = request.body
    signature_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    
    try:
        event = stripe.Webhook.construct_event(
            payload, signature_header, endpoint_secret
        )
    except:
        return HttpResponse(status = 400)
    
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        checkout_session_id = session.client_reference_id
        try:
            order = get_object_or_404(Order, id = checkout_session_id)
        except Order.DoesNotExist:
            return HttpResponse(status=404)
        order.paid = True
        order.save()
    
    return HttpResponse(status=200)