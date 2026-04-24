from django.urls import path
from views.hello_world import hello_world
from views.login import LoginView
<<<<<<< HEAD
from views.order_history import OrderHistory
from views.payment import create_checkout_session, stripe_webhook
=======
>>>>>>> de720c3edb56c8ad6b46383eb4caaa6b0e34d027

urlpatterns = [
    path('users/login/', LoginView.as_view(), name='login'),
    path('hello/', hello_world),
<<<<<<< HEAD

    path('order_history/', OrderHistory.as_view()),

    path('checkout/<int:order_id', create_checkout_session),
    
    path('stripe/webhook', stripe_webhook),

=======
    # path('users/order_history/', OrderHistory.as_view())
>>>>>>> de720c3edb56c8ad6b46383eb4caaa6b0e34d027
]