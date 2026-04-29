from django.urls import path
from apps.views.hello_world import hello_world
from apps.views.login import LoginView
from apps.views.payment import create_checkout_session, stripe_webhook
from apps.views.order_history import View_History, item, reorder


urlpatterns = [
    path('users/login/', LoginView.as_view(), name='login'),
    path('hello/', hello_world),
    path('checkout/<int:order_id>/', create_checkout_session, name='create_checkout_session'),
    path('stripe/webhook', stripe_webhook),
    path('View_History/', View_History, name='View_History'),
    path('View_History/item/<int:id>/', item, name='item'),
    path('reorder/', reorder, name='reorder'),
]