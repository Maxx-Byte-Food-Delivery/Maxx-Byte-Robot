from django.urls import path
from views.views import hello_world
from views.views import LoginView

urlpatterns = [

    path("login/", LoginView.as_view()),

    path('hello/', hello_world)

]