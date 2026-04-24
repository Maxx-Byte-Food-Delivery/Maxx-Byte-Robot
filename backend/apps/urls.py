from django.urls import path
from apps.views import hello_world
from apps.views import LoginView

urlpatterns = [
    path('users/login/', LoginView.as_view(), name='login'),
    path('hello/', hello_world)
]