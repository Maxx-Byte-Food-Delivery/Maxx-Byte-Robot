from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from .order import Order
from .product import Product
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="order_items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)


    @property
    def subtotal(self):
        return self.product.price * self.quantity



   