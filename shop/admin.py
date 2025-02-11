from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    list_filter = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin): 
    list_display = ['title', 'slug', 'image', 'price', 'active', 'created', 'updated']
    list_filter = ['category', 'title', 'active']
    list_editable = ['image', 'active']
    date_hierarchy = 'created'