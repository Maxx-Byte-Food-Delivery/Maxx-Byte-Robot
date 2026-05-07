from django.urls import path
from backend.apps.products.views.products import get_all_products

urlpatterns = [
    path('all_products/', get_all_products, name='get_all_products'),
]