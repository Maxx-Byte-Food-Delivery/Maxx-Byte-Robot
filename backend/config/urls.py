# """Root URL Configuration"""
# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from views.hello_world import hello_world
from views.login import LoginView
from views.login import get_all_products

urlpatterns = [ 
    path('admin/', admin.site.urls),

    path('api/', include("apps.urls")),

    path('login/', LoginView.as_view()),

    path('api/all_products/', get_all_products)
]


