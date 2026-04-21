from django.db import models

# This is for the entire order.
class Order(models.Model):

    customer_name = models.CharField(max_length=30)
    customer_email = models.EmailField(max_length=30)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=15, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

# This is for the items in the order.
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)