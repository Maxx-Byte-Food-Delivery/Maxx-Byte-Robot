import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from apps.models.order import Order
from apps.models.payment import Payment
from apps.models.order_item import OrderItem
from apps.models.product import Product

@pytest.fixture
#makes user
def user(db):
  user = User.objects.create_user(username="johndoe", email= "johndoe@email.com", first_name="john", last_name="doe", password="psswrd123!")
  user.save()
  return user
#makes multiple users
@pytest.fixture
def users(db):
  user1 = User.objects.create_user(username="johndoe", email= "johndoe@email.com", first_name="john", last_name="doe", password ="psswrd123!")
  user2 = User.objects.create_user(username="janedoe", email= "janedoe@email.com", first_name="jane", last_name="doe", password ="SomeG00dPasswor!d")
  user3 = User.objects.create_user(username="SomeUser", email= "someuser@email.com", first_name="some", last_name="user", password="G00dPassw0rd!")
  user1.save()
  user2.save()
  user3.save()
  return [user1, user2, user3]

#creates order with user
@pytest.fixture
def create_order(db, user):
  user_order = Order.objects.create(user=user, total_price=100.00)
  user_order.save()
  return user_order

@pytest.fixture
def create_payment(db, create_order):
  payment = Payment.objects.create(order=create_order, method='card', amount=100.00, transaction_id='abc123', status='pending')
  payment.save()
  return payment

@pytest.fixture
def order_item(db, create_order, create_products):
  order_item = OrderItem.objects.create(order=create_order, product=create_products[0], quantity=2, price=50.00)
  order_item.save()
  return order_item

@pytest.fixture
def create_products(db):
  product1 = Product.objects.create(name="Test Product 1", description="Description for Test Product 1", price=19.99)
  product2 = Product.objects.create(name="Test Product 2", description="Description for Test Product 2", price=29.99)
  return [product1, product2]

@pytest.fixture
def api_client():
  return APIClient()