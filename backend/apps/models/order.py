from django.db import models

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('cancelled', 'Cancelled'),
    ("ready", "Ready"),
    ("preparing", "Preparing"),
    ("dispatched", "Dispatched"),
    ("delivered", "Delivered"),
    ("completed", "Completed")
]

# This is for the entire order.
class Order(models.Model):

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)


    #E nable with Active Order
    delivery_location = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    estimated_delivery_time = models.DateTimeField(null=True, blank=True)
    robot_assigned = models.BooleanField(default=False)