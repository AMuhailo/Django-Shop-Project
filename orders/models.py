from django.db import models

from shop.models import Product

# Create your models here.
class Order(models.Model):
    #Info person
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField()
    
    #Location
    adress = models.CharField(max_length = 100)
    city = models.CharField(max_length = 255)
    postal_code= models.CharField(max_length = 20)
    
    #Created orders
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    paid = models.BooleanField(default = False)
    
    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields = ['-created'])]
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    
    def get_total_money(self):
        return sum(item.get_money() for item in self.items_order.all())
        

class Items(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'items_product')
    order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = 'items_order')
    quantity = models.PositiveIntegerField(default = 1)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    
    def __str__(self):
        return f"{self.order}|{self.id}"
    
    def get_money(self):
        return self.price * self.quantity