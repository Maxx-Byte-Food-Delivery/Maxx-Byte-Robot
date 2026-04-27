from django.urls import path
from apps.views.hello_world import hello_world
from apps.views.login import LoginView
from apps.views.payment import create_checkout_session, stripe_webhook
from apps.views.verify_MFA_view import VerifyMFAView


urlpatterns = [
    path('users/login/', LoginView.as_view(), name='login'),
    path('hello/', hello_world),
    path('checkout/<int:order_id>/', create_checkout_session, name='create_checkout_session'),
    path('stripe/webhook', stripe_webhook),
    path("verify-mfa/", VerifyMFAView.as_view(), name="verify-mfa")
]