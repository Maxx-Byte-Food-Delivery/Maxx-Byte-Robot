from django.urls import path
from apps.views.hello_world import hello_world
from apps.views.login import LoginView
from apps.views.payment import create_checkout_session, stripe_webhook
from apps.views.products import get_all_products
from apps.views.order_history import View_History, item, reorder


urlpatterns = [
    path('users/login/', LoginView.as_view(), name='login'),
    path('hello/', hello_world),
    path('checkout/', create_checkout_session, name='create_checkout_session'),
    path('stripe/webhook', stripe_webhook),
    path('all_products/', get_all_products, name='get_all_products'),
    path('checkout/<int:order_id>/', create_checkout_session, name='create_checkout_session'),
    path('stripe/webhook', stripe_webhook),
    path('users/<int:user_id>/orders/view_history/', View_History, name='view_history'),
    path('users/<int:user_id>/orders/view_history/item/<int:id>/', item, name='view_history_item'),
    path('users/<int:user_id>/orders/reorder/<int:id>/', reorder, name='reorder'),
]