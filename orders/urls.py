from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('',views.create_order, name = 'create_order_url')
]
