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
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    address = models.CharField(max_length=255, default="")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending') # Active, Preparing, Shipped, Delivered
    created_at = models.DateTimeField(auto_now_add=True)

    def update_total(self):
        items = self.order_items.all()
        self.total_price = sum(item.price for item in items)
        self.save(update_fields=['total_price'])


