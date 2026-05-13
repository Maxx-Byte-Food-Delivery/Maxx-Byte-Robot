import random
from datetime import timedelta
from django.conf import settings
from django.utils import timezone

from twilio.rest import Client

from apps.users.models.profile import Profile


def send_mfa_code(user):

    profile = user.profile

    if not profile.phone_number:
        raise ValueError("Phone number not set")
    
    code = str(random.randint(100000, 999999))
    #code = "123456"

    profile.mfa_code = code
    profile.mfa_expiry = (
        timezone.now() + timedelta(minutes=5)
    )

    profile.save()

    # TEMP SMS simulation
    print("SMS CODE:", code)
    print("PHONE:", profile.phone_number)

    #client = Client(
        #settings.TWILIO_ACCOUNT_SID,
        #settings.TWILIO_AUTH_TOKEN
    #)

    #client.messages.create(
        #body=f"Your login code is {code}",
        #from_=settings.TWILIO_PHONE_NUMBER,
        #to=profile.phone_number
    #)