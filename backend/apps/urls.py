from django.urls import path
from .views import hello_world
from .views import LoginView
from .views import order_history


urlpatterns = [

    path("login/", LoginView.as_view()),

    path('hello/', hello_world),

    path('order_history/', order_history)

]