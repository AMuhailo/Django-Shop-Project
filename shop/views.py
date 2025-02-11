from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from cart.forms import QuantityForm
from .forms import ProductCreateFormset
from .models import Category, Product

# Create your views here.


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'pages/shopsitems.html'
    
    def get_queryset(self):
        products = Product.objects.filter(active=True)
        category_slug = self.kwargs.get('category_slug')
        category_id = self.kwargs.get('category_id')
        if category_slug and category_id:
            self.category = get_object_or_404(Category,
                                         slug = category_slug,
                                         id = category_id)
            products = products.filter(category = self.category)
        else:
            self.category = None
        return products
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["category"] = self.category
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateFormset
    template_name = 'pages/forms/createproduct.html'
    success_url = reverse_lazy('shop:product_list_url')
    

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductCreateFormset
    template_name = "pages/forms/createproduct.html"
    success_url = reverse_lazy('shop:product_list_url')
    
    def get_object(self, queryset = ...):
        return get_object_or_404(Product, id = self.kwargs.get('product_id'))
    

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = "pages/detailitem.html"
    slug_url_kwarg = "product_slug"
    pk_url_kwarg = "product_id"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = QuantityForm()
        return context
    