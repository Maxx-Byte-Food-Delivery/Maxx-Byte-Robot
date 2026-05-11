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

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('csrf/', csrf_view),
    path("verify-mfa/", VerifyMFAView.as_view(), name="verify-mfa"),
    path("logout/", logout_view, name="logout"),
    path('verify-2fa/', Verify2FAView.as_view()),
    path('setup-totp/', SetupTOTPView.as_view()),
    path('enable-sms-2fa/', EnableSMS2FAView.as_view()),
    path('disable-2fa/', Disable2FAView.as_view()),
    path('user-profile/', UserProfileView.as_view()),
    path('confirm-totp/', ConfirmTOTPView.as_view()),
]