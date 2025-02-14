from django.urls import path
from . import views

app_name = 'payment'
urlpatterns = [
    path('',views.payment_process, name = 'payment_process_url'),
    path('success/', views.success, name = 'success_url'),
    path('cancel/', views.cancel, name = 'cancel_url'),
]
