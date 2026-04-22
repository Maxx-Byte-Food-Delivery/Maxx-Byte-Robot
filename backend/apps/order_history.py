from django.db import models
from django.contrib.auth.models import User

class BaseHistory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

    class Meta:
        abstract = True  # Tells Django not to create a database table for this class

class Order(BaseHistory):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['-created_at'] # Shows newest orders first