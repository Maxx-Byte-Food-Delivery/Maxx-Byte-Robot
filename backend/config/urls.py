# """Root URL Configuration"""
# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from backend.views.views import hello_world
from backend.views.views import LoginView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("apps.urls")),
]


