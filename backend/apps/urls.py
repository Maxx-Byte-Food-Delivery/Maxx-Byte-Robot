from django.urls import path
from backend.views.views import hello_world
from backend.views.views import LoginView

urlpatterns = [

    path("login/", LoginView.as_view()),

    path('hello/', hello_world)

]