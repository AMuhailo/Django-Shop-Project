from django.shortcuts import render, redirect
from .models import Coupon
from .forms import CouponForm
from django.utils import timezone
from django.views.decorators.http import require_POST
# Create your views here.

@require_POST
def coupons(request):
    form = CouponForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        try:
            coupon = Coupon.objects.get(code__iexact=cd['code'],
                                       valid_from__lte = timezone.now(),
                                       valid_to__gte = timezone.now(),
                                       active = True)
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect("cart:carts_url")