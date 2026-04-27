# """Root URL Configuration"""
# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.views import hello_world
from apps.views import LoginView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("apps.urls")),
]


