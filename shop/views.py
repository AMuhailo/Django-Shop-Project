from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.postgres.search import SearchVector
from django.db.models import Count
from django.utils import timezone
from cart.forms import QuantityForm
from .forms import ProductCreateFormset, SearchForm
from .models import Category, Product, Allowance

# Create your views here.


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'pages/shopsitems.html'
    
    def get_queryset(self):
        products = Product.objects.filter(active=True)\
                                    .select_related('category')
        category_slug = self.kwargs.get('category_slug')
        category_id = self.kwargs.get('category_id')
        if category_slug and category_id:
            self.category = get_object_or_404(Category,
                                         slug = category_slug,
                                         id = category_id)
            products = products.filter(category = self.category).select_related('category')
        else:
            self.category = None
        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = SearchForm() 
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
        product = Product.objects.select_related('category')
        product = get_object_or_404(product, slug = self.kwargs.get('product_slug'),
                                    id = self.kwargs.get('product_id'))
        product_ids = product.category
        similar_product = self.model.objects.filter(category_id__in= [product_ids]).exclude(id = product.id)[:4]
        context['similar_product'] = similar_product
        context["form"] = QuantityForm()
        return context

def search(request):
    query = None
    search_form = SearchForm()
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(active=True).annotate(search = SearchVector('title','description')).filter(search=query)
    context ={
        'query':query,
        'results':results,
        'search_form':search_form
    }
    return render(request,'pages/searchpage.html', context)