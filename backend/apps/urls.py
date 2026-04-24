from django.urls import path
<<<<<<< HEAD
from backend.apps.views.views import hello_world
from backend.apps.views.views import LoginView
=======
from backend.views.views import hello_world
from backend.views.views import LoginView
>>>>>>> 52c8c5c9e76f7625dd5d1076624f41d611b138ad

urlpatterns = [

    path("login/", LoginView.as_view()),

    path('hello/', hello_world)

]