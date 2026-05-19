from django.contrib import admin
from django.urls import path, include
from django_otp.admin import OTPAdminSite
from apps.users.views.csrf import csrf_view

admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/csrf/', csrf_view, name='csrf_token'),
    path('api/users/', include("apps.users.urls")),
    path('api/orders/', include("apps.orders.urls")),
    path('api/payments/', include('apps.payments.urls')),
    path('api/products/', include('apps.products.urls')),
    path('api-auth/', include('rest_framework.urls')),
]