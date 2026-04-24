
import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.models.product import Product

product1 = Product(id=1, name='Hamburger and fries', price = 9.99, description = 'Juicy hamburger with crispy fries')
product2 = Product(id=2, name='Pizza', price = 11.99, description = 'Delicious pizza with your favorite toppings')
product3 = Product(id=3, name='Salad', price = 6.99, description = 'Fresh salad with a variety of vegetables')
product4 = Product(id=4, name='Soda', price = 2.99, description = 'Refreshing carbonated beverage')
product_list = [product1, product2, product3, product4]
for x in product_list:
    x.save()