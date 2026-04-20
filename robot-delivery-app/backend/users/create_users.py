#!/usr/bin/env python3
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robot_delivery_app.settings')
django.setup()

from django.contrib.auth.models import User

user_data = {
    "username": "alice_johnson",
    "password": "Alice@123",
    "email": "alice@maxxbyte.com",
    "first_name": "Alice",
    "last_name": "Johnson"
}

if not User.objects.filter(username=user_data["username"]).exists():
    User.objects.create_user(**user_data)
    print(f"✅ Created: {user_data['username']}")
else:
    print(f"⚠️ Already exists: {user_data['username']}")
