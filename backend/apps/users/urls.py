from django.urls import path
from apps.users.views.csrf import csrf_view
from apps.users.views.login import LoginView
from apps.users.views.verify_mfa import VerifyMFAView
from apps.users.views.logout import logout_view
from apps.users.views.verify_2fa import Verify2FAView
from apps.users.views.setup_totp import SetupTOTPView
from apps.users.views.enable_sms_2fa import EnableSMS2FAView
from apps.users.views.disable_2fa import Disable2FAView
from apps.users.views.user_profile import UserProfileView
from apps.users.views.confirm_totp import ConfirmTOTPView
from apps.users.views.trigger_mfa import MFATriggerView
from apps.users.views.resend_mfa_code import ResendMFAView

urlpatterns = [
    path('users/login/', LoginView.as_view(), name='login'),
    path('csrf/', csrf_view, name='csrf_token'),
    path("users/verify-mfa/", VerifyMFAView.as_view(), name="verify-mfa"),
    path("users/logout/", logout_view, name="logout"),
    path('users/verify-2fa/', Verify2FAView.as_view()),
    path('users/setup-totp/', SetupTOTPView.as_view()),
    path('users/enable-sms-2fa/', EnableSMS2FAView.as_view()),
    path('users/disable-2fa/', Disable2FAView.as_view()),
    path('users/profile/', UserProfileView.as_view()),
    path('users/confirm-totp/', ConfirmTOTPView.as_view()),
    path('users/mfa-trigger/', MFATriggerView.as_view()),
    path("users/resend-mfa/", ResendMFAView.as_view()),
    ]