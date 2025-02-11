from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
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
    
    