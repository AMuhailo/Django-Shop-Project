from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('add/<product_id>/', views.cart_add, name = 'cart_add'),
    path('remove/<product_id>/', views.cart_remove, name = 'cart_remove'),
    path('', views.carts, name = 'carts_url')
]
