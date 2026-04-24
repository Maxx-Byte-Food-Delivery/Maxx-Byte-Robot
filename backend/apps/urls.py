from django.urls import path
from views.hello_world import hello_world
from views.login import LoginView
from views.order_history import order_history

urlpatterns = [
    path('users/login/', LoginView.as_view(), name='login'),
    path('hello/', hello_world),
    path('order_history/', order_history)
]