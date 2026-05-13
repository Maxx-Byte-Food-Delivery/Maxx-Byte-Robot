# """Root URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from two_factor.urls import urlpatterns as tf_urls
# from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django_otp.admin import OTPAdminSite

# Use the OTP admin site
admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/users/', include("apps.users.urls")),

    path('api/orders/', include("apps.orders.urls")),

    path('api/payments/', include('apps.payments.urls')),

    path('api/products/', include('apps.products.urls')),

    path('api-auth/', include('rest_framework.urls')),
]


