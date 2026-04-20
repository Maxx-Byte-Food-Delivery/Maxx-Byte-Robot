import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

from django.contrib.auth.models import User

# 10 Test Users
users = [
    ("alice_johnson", "Alice@123", "alice@maxxbyte.com", "Alice", "Johnson"),
    ("bob_smith", "Bob@456", "bob@maxxbyte.com", "Bob", "Smith"),
    ("carol_davis", "Carol@789", "carol@maxxbyte.com", "Carol", "Davis"),
    ("david_wilson", "David@101", "david@maxxbyte.com", "David", "Wilson"),
    ("emma_brown", "Emma@202", "emma@maxxbyte.com", "Emma", "Brown"),
    ("frank_miller", "Frank@303", "frank@maxxbyte.com", "Frank", "Miller"),
    ("grace_lee", "Grace@404", "grace@maxxbyte.com", "Grace", "Lee"),
    ("henry_taylor", "Henry@505", "henry@maxxbyte.com", "Henry", "Taylor"),
    ("isabel_martin", "Isabel@606", "isabel@maxxbyte.com", "Isabel", "Martin"),
    ("jack_anderson", "Jack@707", "jack@maxxbyte.com", "Jack", "Anderson"),
]

created = 0
for username, password, email, first, last in users:
    if not User.objects.filter(username=username).exists():
        User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first,
            last_name=last
        )
        print(f"✅ Created: {username}")
        created += 1
    else:
        print(f"⚠️ Exists: {username}")

print(f"\n🎉 {created} users created successfully!")
