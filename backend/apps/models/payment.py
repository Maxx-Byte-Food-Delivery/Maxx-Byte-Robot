from backend.apps.models import users
from backend.apps.models import order


class Payment(users.Model):

    PAYMENT_METHODS = [
        ('card', 'Card'),
        ('paypal', 'PayPal'),
        ('apple', 'Apple Pay')
    ]

    order = users.OneToOneField(order.Order, on_delete=users.CASCADE)
    method = users.CharField(max_length=10, choices=PAYMENT_METHODS)
    amount = users.DecimalField(max_digits=8, decimal_places=2)
    transaction_id = users.CharField(max_length=100)
    status = users.CharField(max_length=20, default='pending')
    created_at = users.DateTimeField(auto_now_add=True)