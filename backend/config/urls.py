# """Root URL Configuration"""
# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
<<<<<<< HEAD
from backend.apps.views.views import hello_world
from backend.apps.views.views import LoginView
=======
from backend.views.views import hello_world
from backend.views.views import LoginView
>>>>>>> 52c8c5c9e76f7625dd5d1076624f41d611b138ad



urlpatterns = [ 
    path('admin/', admin.site.urls),

    path('api/', include("apps.urls")),

]


