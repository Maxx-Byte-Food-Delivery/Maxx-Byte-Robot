import random
from datetime import timedelta
from django.conf import settings
from django.utils import timezone

from twilio.rest import Client

from apps.models.profile import Profile


def send_mfa_code(user):

    profile = user.profile

    code = str(random.randint(100000, 999999))

    profile.mfa_code = code
    profile.mfa_expiry = (
        timezone.now() + timedelta(minutes=5)
    )

    profile.save()

    # TEMP SMS simulation
    print("MFA CODE:", code)

    #client = Client(
        #settings.TWILIO_ACCOUNT_SID,
        #settings.TWILIO_AUTH_TOKEN
    #)

    #client.messages.create(
        #body=f"Your login code is {code}",
        #from_=settings.TWILIO_PHONE_NUMBER,
        #to=profile.phone_number
    #)