from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Coupon(models.Model):
    
    #Created name coupon
    code = models.CharField(max_length=20)
    
    #Discount coupon
    discount = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    
    #Active discount
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField()
    
    def __str__(self):
        return self.code