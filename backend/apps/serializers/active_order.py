from rest_framework import serializers
from apps.models.active_order import ActiveOrder


class ActiveOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActiveOrder
        fields = "__all__"