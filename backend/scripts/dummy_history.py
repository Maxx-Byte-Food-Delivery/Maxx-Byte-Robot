import os
import django
import sys
from decimal import Decimal

# 1. Setup
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"
django.setup()

from django.contrib.auth.models import User
from apps.products.models.product import Product
from apps.orders.models.order import Order
from apps.orders.models.order_item import OrderItem

# 2. Create Products (Using your list)
p1 = Product.objects.update_or_create(id=1, defaults={'name': 'Hamburger and fries', 'price': 9.99, 'description': 'Juicy hamburger with crispy fries'})[0]
p2 = Product.objects.update_or_create(id=2, defaults={'name': 'Pizza', 'price': 11.99, 'description': 'Delicious pizza with your favorite toppings'})[0]
p3 = Product.objects.update_or_create(id=3, defaults={'name': 'Salad', 'price': 6.99, 'description': 'Fresh salad with a variety of vegetables'})[0]
p4 = Product.objects.update_or_create(id=4, defaults={'name': 'Soda', 'price': 2.99, 'description': 'Refreshing carbonated beverage'})[0]

# 3. Get/Create User (Matches your frontend localStorage userId)
user, _ = User.objects.get_or_create(username="customer1", email="test@test.com")

# 4. Create an Order
# This matches the "View Order History" row structure
order = Order.objects.create(
    user=user,
    address="123 Maple Avenue",
    total_price=Decimal("22.97"), # p1 + p2 + p3 + p4
    status="completed"
)

# 5. Create OrderItems (The bridge between Order and Product)
# This is what order.order_items.map() in React looks for
OrderItem.objects.create(order=order, product=p1, quantity=1, price=p1.price)
OrderItem.objects.create(order=order, product=p2, quantity=1, price=p2.price)
OrderItem.objects.create(order=order, product=p3, quantity=1, price=p3.price)
OrderItem.objects.create(order=order, product=p4, quantity=1, price=p4.price)

print(f"Created Order #{order.id} for {user.username} with {order.order_items.count()} items.")