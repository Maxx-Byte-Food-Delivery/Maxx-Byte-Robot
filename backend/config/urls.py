# """Root URL Configuration"""
# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.views import hello_world
from apps.views import LoginView
from apps.views import get_all_products
from backend.apps.views.views import hello_world
from backend.apps.views.views import LoginView
from backend.apps.views.views import get_all_products



urlpatterns = [ 
    path('admin/', admin.site.urls),

    path('api/', include("apps.urls")),

    path('login/', LoginView),

    path('api/all_products/', get_all_products)
]


