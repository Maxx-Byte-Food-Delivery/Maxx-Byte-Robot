# """Root URL Configuration"""
# from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from views.products import get_all_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("apps.urls")),
    path('api/all_products/', get_all_products)
]


