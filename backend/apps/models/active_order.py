from django.db import models


class OrderStatus(models.TextChoices):
    PLACED = 'P', ('Placed')
    CONFIRMED = 'C', ('Confirmed')
    PREPAIRING = 'PRE', 


