from decimal import Decimal
from django.conf import settings
from coupons.models import Coupon
from shop.models import Product


class Cart():
    
    #Data initialization
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_API)
        if not cart:
            cart = self.session[settings.CART_SESSION_API] = {}
        self.cart = cart
        self.coupon_id = self.session.get('coupon_id')
    
    #Add to cart
    def add(self, product, quantity = 1, override_quantity = False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity":0,
                                       "price":str(product.total_price())}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
        
    #Save in cart
    def save(self):
        self.session.modified = True
        
    #Remove from cart
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            
    #Iterations in copy cart
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    #Length items in cart
    def __len__(self):            
        return sum(item['quantity'] for item in self.cart.values())
    
    #All price
    def get_total_price(self):
        return sum(item['quantity'] * Decimal(item['price']) for item in self.cart.values())
    
    #Clear cart
    def clear(self):
        del self.session[settings.CART_SESSION_API]
        self.save()
        
    #Take coupon id
    @property
    def coupon(self):
        if self.coupon_id:
            try:
                return Coupon.objects.get(id = self.coupon_id)
            except Coupon.DoesNotExist:
                pass
        return None
    
    #Used coupon id for find discount
    def get_coupon_discount(self):
        if self.coupon:
            return self.coupon.discount / Decimal('100') * self.get_total_price()
        
        return Decimal(0)
    
    #All price with discount
    def get_coupon_discount_total_price(self):
        return self.get_total_price() - self.get_coupon_discount()