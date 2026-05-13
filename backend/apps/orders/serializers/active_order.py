from rest_framework import serializers
from apps.orders.models import Order
from apps.orders.models.order_item import OrderItem

class ActiveOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'total_price', 'status', 'user', 'created_at']