from django.urls import path;
from backend.apps.payments.views.payment import create_checkout_session, stripe_webhook;

urlpatterns = [
    path('checkout/<int:order_id>/', create_checkout_session, name='create_checkout_session'),
    path('stripe/webhook', stripe_webhook),
]