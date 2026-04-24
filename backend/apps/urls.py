from django.urls import path
from views.views import hello_world
from views.views import LoginView

urlpatterns = [
    path('users/login/', LoginView.as_view(), name='login'),
    path('hello/', hello_world)
]