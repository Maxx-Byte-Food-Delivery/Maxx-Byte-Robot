from django.urls import path;
from apps.orders.views.order_history import View_History, item, reorder
from apps.orders.views.active_order import active_order, active_orders
from apps.orders.views.order import create_order

urlpatterns = [
    path('create/', create_order, name='create_order'),
    path('view_history/', View_History, name='view_history'),
    path('view_history/item/<int:id>/', item, name='view_history_item'),
    path('reorder/<int:id>/', reorder, name='reorder'),
    path('active-orders/<int:order_id>/', active_order, name='active_order'),
    path('active-orders/', active_orders, name='active_orders'),
]
