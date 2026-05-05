# """Root URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include("apps.urls")),

    path('api-auth/', include('rest_framework.urls')),

    path('', include(tf_urls)),
]


