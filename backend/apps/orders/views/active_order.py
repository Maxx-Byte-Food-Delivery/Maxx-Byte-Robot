from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.orders.models import Order
from apps.serializers.active_order import ActiveOrderSerializer


class ActiveOrderView(APIView):
    # GET: List all active orders
    def get(self, request, user_id,order_id):
        try:
            order = Order.objects.get(id = order_id, user_id = user_id, status = "active")

            serializer = ActiveOrderSerializer(order)
            return Response(serializer.data)

        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    

    def patch(self, request, user_id, order_id):
        try:
            order = Order.objects.get(
                id=order_id,
                user_id=user_id
            )

            serializer = ActiveOrderSerializer(order, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)