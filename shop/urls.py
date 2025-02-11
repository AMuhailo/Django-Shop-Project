from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.ProductListView.as_view(), name = 'product_list_url'),
    path('category/<category_slug>/<category_id>/', views.ProductListView.as_view(), name = 'category_product_list_url'),
]
