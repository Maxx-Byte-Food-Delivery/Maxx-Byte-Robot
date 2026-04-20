from django.db import models
from django.conf import settings
from simple_history.models import HistoricalRecords


class AbstractOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    
    # Tracks all model changes automatically
    history = HistoricalRecords(inherit=True) 

    class Meta:
        abstract = True  # Makes this an abstract base class

class Order(AbstractOrder):
    # Specific fields for this order implementation
    order_name = models.CharField(max_length=100)



