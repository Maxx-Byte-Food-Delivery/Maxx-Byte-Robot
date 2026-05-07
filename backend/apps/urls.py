from django.urls import path
from apps.users.views.csrf import csrf_view
from apps.users.views.login import LoginView
from apps.payments.views.payment import create_checkout_session, stripe_webhook
from apps.users.views.verify_MFA_view import VerifyMFAView
from apps.users.views.logout import logout_view
from apps.users.views.verify_2fa import Verify2FAView
from apps.users.views.setup_totp import SetupTOTPView
from apps.users.views.enable_sms_2fa import EnableSMS2FAView
from apps.users.views.disable_2fa import Disable2FAView
from apps.users.views.user_profile import UserProfileView
from apps.users.views.confirm_totp import ConfirmTOTPView
from apps.users.views.verify_sms import VerifySMSView


from apps.products.views.products import get_all_products
from apps.orders.views.order_history import View_History, item, reorder


urlpatterns = [
    path('users/login/', LoginView.as_view(), name='login'),
    path('csrf/', csrf_view),
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
    path('user-profile/', UserProfileView.as_view()),
    path('confirm-totp/', ConfirmTOTPView.as_view()),
    path("verify-sms/", VerifySMSView.as_view()),

    
    path('stripe/webhook', stripe_webhook),
    path('users/<int:user_id>/orders/view_history/', View_History, name='view_history'),
    path('users/<int:user_id>/orders/view_history/item/<int:id>/', item, name='view_history_item'),
    path('users/<int:user_id>/orders/reorder/<int:id>/', reorder, name='reorder'),
]