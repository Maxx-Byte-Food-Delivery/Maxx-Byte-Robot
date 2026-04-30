import os
import django

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'config.settings'
)

django.setup()

from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice

import qrcode


# username, password, email, first, last, is_staff
users = [

    ("alice_johnson", "Alice@123",
     "alice@maxxbyte.com",
     "Alice", "Johnson", False),

    ("bob_smith", "Bob@456",
     "bob@maxxbyte.com",
     "Bob", "Smith", False),

    ("carol_davis", "Carol@789",
     "carol@maxxbyte.com",
     "Carol", "Davis", False),

    ("david_wilson", "David@101",
     "david@maxxbyte.com",
     "David", "Wilson", False),

    # STAFF USERS
    ("emma_brown", "Emma@202",
     "emma@maxxbyte.com",
     "Emma", "Brown", True),

    ("frank_miller", "Frank@303",
     "frank@maxxbyte.com",
     "Frank", "Miller", True),

    ("grace_lee", "Grace@404",
     "grace@maxxbyte.com",
     "Grace", "Lee", True),

    ("henry_taylor", "Henry@505",
     "henry@maxxbyte.com",
     "Henry", "Taylor", True),

    ("isabel_martin", "Isabel@606",
     "isabel@maxxbyte.com",
     "Isabel", "Martin", False),

    ("jack_anderson", "Jack@707",
     "jack@maxxbyte.com",
     "Jack", "Anderson", False),

]


# Create folder for QR codes
qr_folder = "qr_codes"

if not os.path.exists(qr_folder):
    os.makedirs(qr_folder)


for username, password, email, first, last, is_staff in users:

    user, created = User.objects.get_or_create(
        username=username
    )

    user.set_password(password)
    user.email = email
    user.first_name = first
    user.last_name = last
    user.is_staff = is_staff

    user.save()

    # Create MFA device
    device, device_created = TOTPDevice.objects.get_or_create(
        user=user,
        name="default",
        defaults={"confirmed": True}
    )

    # Generate QR code
    config_url = device.config_url

    img = qrcode.make(config_url)

    qr_path = os.path.join(
        qr_folder,
        f"{username}_qr.png"
    )

    img.save(qr_path)

    if created:
        print(f"Created user: {username}")
    else:
        print(f"Updated user: {username}")

    if device_created:
        print(f"Created MFA device for: {username}")

print("User + MFA setup complete.")