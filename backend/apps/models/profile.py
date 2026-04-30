from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True
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

    def __str__(self):
        return self.user.username