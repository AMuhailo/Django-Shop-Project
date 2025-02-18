from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.ProductListView.as_view(), name = 'product_list_url'),
    path('category/<category_slug>/<category_id>/', views.ProductListView.as_view(), name = 'category_product_list_url'),
    path('product/add/', views.ProductCreateView.as_view(), name = 'product_create_url'),
    path('product/update/<product_id>', views.ProductUpdateView.as_view(), name = 'product_update_url'),
    path('product/<product_slug>/<product_id>/', views.ProductDetailView.as_view(), name = 'product_detail_url'),
    path('search/',views.search, name = 'search_url')
]
