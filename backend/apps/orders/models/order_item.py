from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
    
class OrderItem(models.Model):
    order = models.ForeignKey('orders.Order', related_name="order_items", on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)


    @property
    def subtotal(self):
        return self.product.price * self.quantity

    def save(self, *args, **kwargs):
        if self.product and self.quantity is not None:
            self.price = self.product.price * self.quantity
        super().save(*args, **kwargs)