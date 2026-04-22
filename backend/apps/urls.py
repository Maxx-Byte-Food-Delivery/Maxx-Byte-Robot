from django.urls import path
from apps.views import hello_world
from apps.views import LoginView

urlpatterns = [

    path("login/", LoginView.as_view()),

    path('hello/', hello_world)

]