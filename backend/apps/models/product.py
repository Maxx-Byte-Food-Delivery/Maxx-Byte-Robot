from django.db import models

# This is for a product listing. 
class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=False)