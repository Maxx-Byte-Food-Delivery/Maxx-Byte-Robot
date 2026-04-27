from django.urls import path
from views.hello_world import hello_world
from views.login import LoginView
from views.order_history import OrderHistory
from views.payment import create_checkout_session, stripe_webhook

urlpatterns = [
    path('users/login/', LoginView.as_view(), name='login'),
    path('hello/', hello_world),

    path('order_history/', OrderHistory.as_view()),

    path('checkout/<int:order_id', create_checkout_session),
    
    path('stripe/webhook', stripe_webhook),

]