from django.db import models
from django.contrib.auth.hashers import make_password
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

# 10 Test Users
test_users = [
    {"username": "alice_johnson", "password": "Alice@123"},
    {"username": "bob_smith", "password": "Bob@456"},
    {"username": "carol_davis", "password": "Carol@789"},
    {"username": "david_wilson", "password": "David@101"},
    {"username": "emma_brown", "password": "Emma@202"},
    {"username": "frank_miller", "password": "Frank@303"},
    {"username": "grace_lee", "password": "Grace@404"},
    {"username": "henry_taylor", "password": "Henry@505"},
    {"username": "isabel_martin", "password": "Isabel@606"},
    {"username": "jack_anderson", "password": "Jack@707"},
]

created = 0
for user in test_users:
    if not User.objects.filter(username=user["username"]).exists():
        User.objects.create(
            username=user["username"],
            password=make_password(user["password"])
        )
        print(f"✅ Created: {user['username']}")
        created += 1
    else:
        print(f"⚠️ Exists: {user['username']}")

print(f"\n✅ {created} users created")
