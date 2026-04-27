from django.urls import path
from .views import hello_world
from .views import LoginView
from .views import order_history


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