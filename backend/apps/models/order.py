from django.db import models

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('cancelled', 'Cancelled')
]

# This is for the entire order.
class Order(models.Model):

    customer_name = models.CharField(max_length=30)
    customer_email = models.EmailField(max_length=30)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)