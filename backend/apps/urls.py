from django.urls import path
from apps.views.hello_world import hello_world
from apps.views.login import LoginView
from apps.views.payment import create_checkout_session, stripe_webhook
from apps.views.verify_MFA_view import VerifyMFAView
from apps.views.logout import logout_view
from apps.views.payment import create_checkout_session, stripe_webhook
from apps.views.verify_2fa import Verify2FAView
from apps.views.setup_totp import SetupTOTPView
from apps.views.enable_sms_2fa import EnableSMS2FAView
from apps.views.disable_2fa import Disable2FAView



urlpatterns = [
    path('users/login/', LoginView.as_view(), name='login'),
    path('hello/', hello_world),
    path('checkout/<int:order_id>/', create_checkout_session, name='create_checkout_session'),
    path('stripe/webhook', stripe_webhook),
    path("verify-mfa/", VerifyMFAView.as_view(), name="verify-mfa"),
    path("logout/", logout_view, name="logout"),
    path('create-checkout-session/<int:order_id>/', create_checkout_session),
    path('stripe-webhook/', stripe_webhook),
    path('verify-2fa/', Verify2FAView.as_view()),
    path('setup-totp/', SetupTOTPView.as_view()),
    path('enable-sms-2fa/', EnableSMS2FAView.as_view()),
    path('disable-2fa/', Disable2FAView.as_view()),
]