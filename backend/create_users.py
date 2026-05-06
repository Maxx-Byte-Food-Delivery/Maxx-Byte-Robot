import os
import django

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'config.settings'
)

django.setup()

from django.contrib.auth.models import User
from apps.models.profile import Profile
from apps.utils.twofa import generate_secret

# username, password, email, first, last, is_staff
users = [
    ("alice_johnson", "Alice@123", "alice@maxxbyte.com", "Alice", "Johnson", False),
    ("bob_smith", "Bob@456", "bob@maxxbyte.com", "Bob", "Smith", False),
    ("carol_davis", "Carol@789", "carol@maxxbyte.com", "Carol", "Davis", False),
    ("david_wilson", "David@101", "david@maxxbyte.com", "David", "Wilson", False),

    # STAFF USERS
    ("emma_brown", "Emma@202", "emma@maxxbyte.com", "Emma", "Brown", True),
    ("frank_miller", "Frank@303", "frank@maxxbyte.com", "Frank", "Miller", True),
    ("grace_lee", "Grace@404", "grace@maxxbyte.com", "Grace", "Lee", True),
    ("henry_taylor", "Henry@505", "henry@maxxbyte.com", "Henry", "Taylor", True),

    ("isabel_martin", "Isabel@606", "isabel@maxxbyte.com", "Isabel", "Martin", False),
    ("jack_anderson", "Jack@707", "jack@maxxbyte.com", "Jack", "Anderson", False),
]

for username, password, email, first, last, is_staff in users:

    user, created = User.objects.get_or_create(username=username)

    user.set_password(password)
    user.email = email
    user.first_name = first
    user.last_name = last
    user.is_staff = is_staff
    user.save()

    profile, _ = Profile.objects.get_or_create(user=user)

    # ======================
    # 👨‍🎓 STUDENTS (NO MFA YET)
    # ======================
    if not is_staff:
        profile.mfa_enabled = False
        profile.mfa_method = None
        profile.mfa_secret = None

    # ======================
    # 👩‍💼 STAFF (MFA ENABLED)
    # ======================
    else:
        profile.mfa_enabled = True
        profile.mfa_method = "sms"

    profile.save()

    if created:
        print(f"Created user: {username}")
    else:
        print(f"Updated user: {username}")

print("User setup complete.")