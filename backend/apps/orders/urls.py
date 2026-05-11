from django.urls import path;
from apps.orders.views.order_history import View_History, item, reorder
from apps.orders.views.active_order import ActiveOrderView

urlpatterns = [
    path('users/<int:user_id>/orders/view_history/', View_History, name='view_history'),
    path('users/<int:user_id>/orders/view_history/item/<int:id>/', item, name='view_history_item'),
    path('users/<int:user_id>/orders/reorder/<int:id>/', reorder, name='reorder'),
    path('users/<int:user_id>/orders/active_order/<int:id>/', ActiveOrderView, name= 'active_order'),
]
