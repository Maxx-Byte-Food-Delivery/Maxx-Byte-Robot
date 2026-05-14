import os
import sys
import django

# Setup Django environment
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"
django.setup()

# Import models after django.setup()
from django.contrib.auth.models import User
from apps.products.models import Product
from apps.orders.models.order import Order
from apps.orders.models.order_item import OrderItem

# Fetch existing dummy data from database
users = list(User.objects.all()[:4])
products = list(Product.objects.all()[:4])

# Ensure enough dummy data exists
if len(users) < 4 or len(products) < 4:
    raise ValueError("You need at least 4 users and 4 products in the database.")

# Create and save orders
order_list = [
    Order(user=users[0]),
    Order(user=users[1]),
    Order(user=users[2]),
    Order(user=users[3])
]
for order in order_list:
    order.save()

# Create and save order items (Notice: No trailing commas, passing object instances)
order_item_list = [
    OrderItem(order=order_list[0], product=products[0]),
    OrderItem(order=order_list[1], product=products[1]),
    OrderItem(order=order_list[2], product=products[2]),
    OrderItem(order=order_list[3], product=products[3])
]
for item in order_item_list:
    item.save()

print("Successfully created 4 dummy orders and items.")