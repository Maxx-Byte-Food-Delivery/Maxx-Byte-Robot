from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
    
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

@receiver(post_save, sender=OrderItem, dispatch_uid="orderitem_post_save_update_total")
@receiver(post_delete, sender=OrderItem, dispatch_uid="orderitem_post_delete_update_total")
def update_order_total(sender, instance, **kwargs):
    instance.order.update_total()