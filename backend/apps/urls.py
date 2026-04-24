from django.urls import path
from views.hello_world import hello_world
from views.login import LoginView
from views.order_history import OrderHistory


urlpatterns = [

    path("login/", LoginView.as_view()),

    path('hello/', hello_world),

    path('order_history/', OrderHistory.as_view())

]