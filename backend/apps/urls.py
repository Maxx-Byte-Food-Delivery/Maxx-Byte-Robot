from django.urls import path
from views.hello import hello_world
from views.login import LoginView

urlpatterns = [
    path('users/login/', LoginView.as_view(), name='login'),
    path('hello/', hello_world)
    path('users/order_history/', OrderHistory.as_view())
]