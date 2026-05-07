from backend.apps import models
from backend.apps.orders import order


class Payment(models.Model):

    PAYMENT_METHODS = [
        ('card', 'Card'),
        ('paypal', 'PayPal'),
        ('apple', 'Apple Pay')
    ]

    order = models.OneToOneField(order.Order, on_delete=models.CASCADE)
    method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)