from django.urls import path
from backend.apps.views.views import hello_world
from backend.apps.views.views import LoginView

urlpatterns = [

    path("login/", LoginView.as_view()),

    path('hello/', hello_world)

]