from django.urls import path
from . import views

app_name = 'coupon'

urlpatterns = [
    path('apply/', views.coupons, name = 'coupons_url'),
]
