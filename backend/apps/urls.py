from django.urls import path

from apps.views.csrf import csrf_view
from apps.views.login import LoginView
from apps.views.payment import stripe_webhook
from apps.views.verify_MFA_view import VerifyMFAView
from apps.views.logout import logout_view
from apps.views.verify_2fa import Verify2FAView
from apps.views.setup_totp import SetupTOTPView
from apps.views.enable_sms_2fa import EnableSMS2FAView
from apps.views.disable_2fa import Disable2FAView
from apps.views.user_profile import UserProfileView
from apps.views.confirm_totp import ConfirmTOTPView
from apps.views.verify_sms import VerifySMSView
from apps.utils.fetch_products import FetchProductsView
from apps.views.products import get_all_products
from apps.views.order_history import View_History, item, reorder

# ✅ ONLY ONE checkout implementation
from apps.views.checkout import CreateCheckoutSessionView


urlpatterns = [

    # ======================
    # AUTH
    # ======================
    path('users/login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

    # ======================
    # SECURITY / MFA
    # ======================
    path('csrf/', csrf_view),
    path("verify-mfa/", VerifyMFAView.as_view(), name="verify-mfa"),
    path('verify-2fa/', Verify2FAView.as_view()),
    path('setup-totp/', SetupTOTPView.as_view()),
    path('confirm-totp/', ConfirmTOTPView.as_view()),
    path("verify-sms/", VerifySMSView.as_view()),
    path('enable-sms-2fa/', EnableSMS2FAView.as_view()),
    path('disable-2fa/', Disable2FAView.as_view()),

    # ======================
    # USER
    # ======================
    path('user-profile/', UserProfileView.as_view()),

    # ======================
    # PRODUCTS
    # ======================
    path('api/products/', FetchProductsView.as_view()),
    path('all_products/', get_all_products, name='get_all_products'),

    # ======================
    # ORDERS / HISTORY
    # ======================
    path('users/<int:user_id>/orders/view_history/', View_History, name='view_history'),
    path('users/<int:user_id>/orders/view_history/item/<int:id>/', item, name='view_history_item'),
    path('users/<int:user_id>/orders/reorder/<int:id>/', reorder, name='reorder'),

    # ======================
    # STRIPE CHECKOUT
    # ======================
    path('create-checkout-session/', CreateCheckoutSessionView.as_view()),

    # ======================
    # STRIPE WEBHOOK (KEEP ONE)
    # ======================
    path('stripe/webhook/', stripe_webhook),
]