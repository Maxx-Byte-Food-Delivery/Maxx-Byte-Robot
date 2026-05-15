def get_mfa_phone(user):
    """
    Returns the correct phone number for MFA SMS delivery.
    Priority:
    1. mfa_phone_number (preferred security channel)
    2. phone_number (SIS fallback)
    """

    profile = user.profile

    if profile.mfa_phone_number:
        return profile.mfa_phone_number

    return profile.phone_number