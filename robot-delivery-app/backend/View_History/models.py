from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
   # total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    products = models.ManyToManyField('Product', through='OrderItem')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    
    def __str__(self):
        if self.user:
            return f"Order {self.id} by {self.user.username}"
        return f"Order {self.id} (No User)"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="order_items", on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    @property
    def subtotal(self):
        return self.product.price * self.quantity



   