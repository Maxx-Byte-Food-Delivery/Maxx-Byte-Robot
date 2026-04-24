from django.urls import path
from apps.views.hello_world import hello_world
from apps.views.login import LoginView

urlpatterns = [
    path('users/login/', LoginView.as_view(), name='login'),
    path('hello/', hello_world),
    # path('users/order_history/', OrderHistory.as_view())
]