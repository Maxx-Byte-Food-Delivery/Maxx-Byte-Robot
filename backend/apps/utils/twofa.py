import pyotp
import random

def generate_secret():
    return pyotp.random_base32()

def get_totp(secret):
    return pyotp.TOTP(secret)

def get_provisioning_uri(user, secret):
    totp = pyotp.TOTP(secret)
    return totp.provisioning_uri(
        name=user.username,
        issuer_name="MaxxByte"
    )