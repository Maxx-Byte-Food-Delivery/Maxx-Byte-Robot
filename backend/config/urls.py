# """Root URL Configuration"""
# from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django_otp.admin import OTPAdminSite

# Use the OTP admin site
admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include("apps.urls")),

    path('api-auth/', include('rest_framework.urls')),
]


