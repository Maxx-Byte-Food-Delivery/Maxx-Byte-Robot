import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from apps.orders.models.order import Order
from apps.payments.models.payment import Payment
from apps.orders.models.order_item import OrderItem
from apps.products.models.product import Product
from apps.users.models.profile import Profile
from apps.utils.twofa import generate_secret
import subprocess
import time
from asgiref.sync import sync_to_async
import os
import shutil
import subprocess
import time
import requests
import socket

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

def is_port_open(host: str, port: int) -> bool:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(0.5)
    return s.connect_ex((host, port)) == 0

@pytest.fixture(scope="session")
def run_react_frontend():
  host = "127.0.0.1"
  port = 5173
  process = None
  if not is_port_open(host, port):
    npm_path = shutil.which("npm")
    if not npm_path:
      pytest.fail("NPM executable not found in system PATH.")

    process = subprocess.Popen(
      [npm_path, "run", "dev", "--", "--port", str(port), "--strictPort"],
      cwd="../frontend",
      stdout=subprocess.DEVNULL,
      stderr=subprocess.DEVNULL,
    )

    timeout = 30
    start_time = time.time()
    server_ready = False

    while time.time() - start_time < timeout:
      if is_port_open(host, port):
        server_ready = True
        break
      time.sleep(0.5)

  if not server_ready:
    process.terminate()
    process.wait()
    pytest.fail(f"Vite server failed to spin up on http://{host}:{port} within {timeout}s")
  yield 

  if process is not None:
    process.terminate()
    try:
      process.wait(timeout=5)
    except subprocess.TimeoutExpired:
      process.kill()

#makes multiple users
@pytest.fixture
def users(db):
  user1 = User.objects.create_user(username="johndoe", email= "johndoe@email.com", first_name="john", last_name="doe", password="VeryG00d!Password")
  user2 = User.objects.create_user(username="janedoe", email= "janedoe@email.com", first_name="jane", last_name="doe", password ="SomeG00dPasswor!d")
  user3 = User.objects.create_user(username="SomeUser", email= "someuser@email.com", first_name="some", last_name="user", password="G00dPassw0rd!")
  user4 = User.objects.create_user(username="student", email= "anotheruser@email.com", first_name="student", last_name="user", password="StudentP@ssw0rd!")
  user1.save()
  user2.save()
  user3.save()
  user4.save()
  return [user1, user2, user3, user4]

@pytest.fixture
def admin_users(db):
  admin_user = User.objects.create_superuser(username="admin", email= "admin@email.com", first_name="admin", last_name="user", password="AdminP@ssw0rd!")
  admin_user2 = User.objects.create_superuser(username="admin2", email= "admin2@email.com", first_name="admin2", last_name="user2", password="AdminP@ssw0rd!")

  return [admin_user, admin_user2]

@pytest.fixture
def student_profiles(db, users):
  user = users[2]
  user2 = users[3]
  
  # TOTP setup
  student_profile, created = Profile.objects.get_or_create(
    user=user,
    defaults={'role': 'student', 'mfa_method': 'totp', 'mfa_enabled': True, 'mfa_secret': generate_secret()}
  )
  if not created:
    student_profile.role = 'student'
    student_profile.mfa_method = 'totp'
    student_profile.mfa_enabled = True
    student_profile.mfa_secret = generate_secret()
    student_profile.save()
  
  # SMS setup
  student_profile2, created = Profile.objects.get_or_create(
    user=user2,
    defaults={'role': 'student', 'mfa_method': 'sms', 'mfa_enabled': True, 'phone_number': "+1555555555"}
  )
  if not created:
    student_profile2.role = 'student'
    student_profile2.mfa_method = 'sms'
    student_profile2.mfa_enabled = True
    student_profile2.phone_number = "+15555555555"
    student_profile2.save()
  
  return [student_profile, student_profile2]

@pytest.fixture
def admin_profiles(db, admin_users):
  admin_user = admin_users[0]
  admin_user2 = admin_users[1]
  
  # TOTP setup
  admin_profile, created = Profile.objects.get_or_create(
    user=admin_user, 
    defaults={'role': 'staff', 'mfa_method': 'totp', 'mfa_enabled': True, 'mfa_secret': generate_secret(), 'phone_number': "+15555555555"}
  )
  if not created:
    admin_profile.role = 'staff'
    admin_profile.mfa_method = 'totp'
    admin_profile.mfa_enabled = True
    admin_profile.mfa_secret = generate_secret()
    admin_profile.phone_number = "+15555555555"
    admin_profile.save()
  
  # SMS setup
  admin_profile2, created = Profile.objects.get_or_create(
    user=admin_user2,
    defaults={'role': 'staff', 'mfa_method': 'sms', 'mfa_enabled': True, 'phone_number': "+15555555555"}
  )
  if not created:
    admin_profile2.role = 'staff'
    admin_profile2.mfa_method = 'sms'
    admin_profile2.mfa_enabled = True
    admin_profile2.phone_number = "+15555555555"
    admin_profile2.save()
  
  return [admin_profile, admin_profile2]

#makes multiple orders
@pytest.fixture(scope="function")
def create_orders(db, users):
  order1 = Order.objects.create(user=users[0])
  order2 = Order.objects.create(user=users[1])
  order3 = Order.objects.create(user=users[2])
  order4 = Order.objects.create(user=users[0])
  order1.save()
  order2.save()
  order3.save()
  order4.save()
  return [order1, order2, order3, order4]

@pytest.fixture
def create_payment(db, create_orders, order_items):
  order = create_orders[0]
  order.refresh_from_db()
  payment = Payment.objects.create(order=order, method='card', transaction_id='abc123', status='pending', amount=order.total_price,)
  
  return payment

@pytest.fixture(scope="function")
def order_items(db, create_orders, create_products):
    def create_item(order, product, qty):
        return OrderItem.objects.create(
            order=order,
            product=product,
            quantity=qty,
        )

    items = [
        create_item(create_orders[0], create_products[0], 2),
        create_item(create_orders[1], create_products[1], 1),
        create_item(create_orders[2], create_products[0], 3),
        create_item(create_orders[2], create_products[1], 1),
    ]
    return items

@pytest.fixture(scope="function")
def create_products(db):
  product1 = Product.objects.create(name="Test Product 1", description="Description for Test Product 1", price=19.99)
  product2 = Product.objects.create(name="Test Product 2", description="Description for Test Product 2", price=29.99)
  return [product1, product2]

@pytest.fixture
def api_client():
  return APIClient()

