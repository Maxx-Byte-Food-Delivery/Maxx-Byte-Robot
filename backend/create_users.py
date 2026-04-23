import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from users.models import User
from django.contrib.auth.hashers import make_password

# 18 users (8 staff + 10 students)
users = [
    # Staff users
    ("james_wilson", "Staff@123", "james.wilson@university.edu", "James", "Wilson"),
    ("maria_garcia", "Staff@456", "maria.garcia@university.edu", "Maria", "Garcia"),
    ("david_park", "Staff@789", "david.park@university.edu", "David", "Park"),
    ("lisa_rodriguez", "Staff@101", "lisa.rodriguez@university.edu", "Lisa", "Rodriguez"),
    ("kevin_zhang", "Staff@202", "kevin.zhang@university.edu", "Kevin", "Zhang"),
    ("jose_garcia", "Staff@303", "jose.garcia@university.edu", "Jose", "Garcia"),
    ("lisa_thomas", "Staff@404", "lisa.thomas@university.edu", "Lisa", "Thomas"),
    ("carlos_rodriguez", "Staff@505", "carlos.rodriguez@university.edu", "Carlos", "Rodriguez"),
    # Student users
    ("alice_johnson", "Student@123", "alice.johnson@university.edu", "Alice", "Johnson"),
    ("bob_smith", "Student@456", "bob.smith@university.edu", "Bob", "Smith"),
    ("carol_davis", "Student@789", "carol.davis@university.edu", "Carol", "Davis"),
    ("david_wilson", "Student@101", "david.wilson@university.edu", "David", "Wilson"),
    ("emma_brown", "Student@202", "emma.brown@university.edu", "Emma", "Brown"),
    ("frank_miller", "Student@303", "frank.miller@university.edu", "Frank", "Miller"),
    ("grace_lee", "Student@404", "grace.lee@university.edu", "Grace", "Lee"),
    ("henry_taylor", "Student@505", "henry.taylor@university.edu", "Henry", "Taylor"),
    ("isabel_martin", "Student@606", "isabel.martin@university.edu", "Isabel", "Martin"),
    ("jack_anderson", "Student@707", "jack.anderson@university.edu", "Jack", "Anderson"),
]

created = 0
for username, password, email, first, last in users:
    if not User.objects.filter(username=username).exists():
        User.objects.create(
            username=username,
            password=make_password(password),
            email=email,
            first_name=first,
            last_name=last
        )
        print(f"✅ Created: {username} ({email})")
        created += 1
    else:
        print(f"⚠️ Exists: {username}")

print(f"\n🎉 {created} users created successfully!")
print(f"📧 All emails: @university.edu")
