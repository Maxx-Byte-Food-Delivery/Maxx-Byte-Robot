import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


import django

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'config.settings'
)

django.setup()

from django.contrib.auth.models import User
from apps.users.models.profile import Profile
from apps.utils.twofa import generate_secret

# username, password, email, first, last, is_staff, phone
users = [
    ("alice_johnson", "Alice@123", "alice@maxxbyte.com", "Alice", "Johnson", False, "+17575550101"),
    ("bob_smith", "Bob@456", "bob@maxxbyte.com", "Bob", "Smith", False, "+17575550102"),
    ("carol_davis", "Carol@789", "carol@maxxbyte.com", "Carol", "Davis", False, "+17575550103"),
    ("david_wilson", "David@101", "david@maxxbyte.com", "David", "Wilson", False, "+17575550104"),

    # STAFF USERS
    ("emma_brown", "Emma@202", "emma@maxxbyte.com", "Emma", "Brown", True, "+17575550105"),
    ("frank_miller", "Frank@303", "frank@maxxbyte.com", "Frank", "Miller", True, "+17575550106"),
    ("grace_lee", "Grace@404", "grace@maxxbyte.com", "Grace", "Lee", True, "+17575550107"),
    ("henry_taylor", "Henry@505", "henry@maxxbyte.com", "Henry", "Taylor", True, "+17575550108"),

    ("isabel_martin", "Isabel@606", "isabel@maxxbyte.com", "Isabel", "Martin", False, "+17575550109"),
    ("jack_anderson", "Jack@707", "jack@maxxbyte.com", "Jack", "Anderson", False, "+17575550110"),
]

for username, password, email, first, last, is_staff, phone_number in users:

    user, created = User.objects.get_or_create(username=username)

    user.set_password(password)
    user.email = email
    user.first_name = first
    user.last_name = last
    user.is_staff = is_staff
    user.save()

    profile, _ = Profile.objects.get_or_create(user=user)
    
    # Save phone number
    profile.phone_number = phone_number

    # default MFA phone = SIS phone
    profile.mfa_phone_number = phone_number


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

        # Optional: generate secret for future TOTP upgrades
        if not profile.mfa_secret:
            profile.mfa_secret = generate_secret()

    profile.save()

    if created:
        print(f"Created user: {username}")
    else:
        print(f"Updated user: {username}")

print("User setup complete.")