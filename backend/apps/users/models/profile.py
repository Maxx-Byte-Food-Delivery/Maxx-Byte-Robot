from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    ROLE_CHOICES = [
    ("student", "Student"),
    ("teacher", "Teacher"),
    ("admin", "Admin"),
    ("it", "IT Support"),
]


    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student")

    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    mfa_method = models.CharField(
        max_length=10,
        choices=[('totp', 'TOTP'), ('sms', 'SMS')],
        null=True,
        blank=True
    )

    mfa_code = models.CharField(
        max_length=6,
        blank=True,
        null=True
    )

    mfa_expiry = models.DateTimeField(
        blank=True,
        null=True
    )

    mfa_enabled = models.BooleanField(
        default=True
    )

    mfa_secret = models.CharField(
        max_length=32, 
        blank=True, 
        null=True
    )
    
    def __str__(self):
        return self.user.username