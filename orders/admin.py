from django.contrib import admin
from .models import Order , Items

# Register your models here.
class ItemAdmin(admin.TabularInline):
    model = Items
    fields = ['product','order','quantity','price']
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'adress', 'city', 'postal_code', 'created', 'updated', 'paid']
    list_filter = ['last_name','postal_code','paid']
    search_fields = ['first_name', 'last_name','postal_code']
    date_hierarchy = 'created'
    inlines = [ItemAdmin]