from django.contrib import admin
from .models import Category, Product, Allowance

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    list_filter = ['title']


class AllowanceInLine(admin.TabularInline):
    model = Allowance
    fields = ['discount','from_date','to_date','active']
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin): 
    list_display = ['title', 'slug', 'image', 'price', 'active', 'created', 'updated']
    list_filter = ['category', 'title', 'active']
    list_editable = ['image', 'active']
    date_hierarchy = 'created'
    inlines=[AllowanceInLine]
    
    
@admin.register(Allowance)
class AllowanceAdmin(admin.ModelAdmin):
    list_display = ['product', 'discount','from_date','to_date','active']
    list_filter = ['from_date','to_date','active']
    list_editable = ['active']
