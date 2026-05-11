from django.urls import path
from apps.products.views.products import ProductListView

urlpatterns = [
    path('all_products/', ProductListView.as_view(), name='get_all_products'),
]