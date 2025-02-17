from decimal import Decimal
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50, blank = True)
    
    class Meta:
        ordering = ['-id','slug']
        indexes = [models.Index(fields = ['-id']),
                   models.Index(fields = ['slug'])]
        verbose_name = 'Category'
        verbose_name_plural = "Categories"
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    
    #Product info
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'category_product')
    image = models.ImageField(upload_to = 'product/',blank = True)
    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length = 255, blank = True)
    description = models.TextField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    active = models.BooleanField(default = True)
    
    #Created product
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ['-id', '-created']
        indexes = [models.Index(fields = ['id', 'slug']),
                    models.Index(fields = ['title']),
                    models.Index(fields = ['-created'])]
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.category}-{self.title}-product")
        return super().save(*args, **kwargs)
    
    def total_price(self):
        try:
            if self.discount_price() < self.price:
                return self.price - self.discount_price()
            return self.price
        except Allowance.DoesNotExist:
            return self.price 
    def discount_price(self):
        try:
            allowance = self.product_allowance.get(from_date__lte=timezone.now(),
                                                        to_date__gte = timezone.now(),
                                                        active = True)
            if allowance:
                return self.price * allowance.discount / Decimal('100')
            return self.price
        except Allowance.DoesNotExist:
            return self.price 
    def __str__(self):
        return self.title
    
class Allowance(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_allowance')
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    active = models.BooleanField()
    
    def __str__(self):
        return f"{self.discount}"