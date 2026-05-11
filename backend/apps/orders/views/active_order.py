from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.orders.models import Order
from apps.serializers.active_order import ActiveOrderSerializer


class ActiveOrderView(APIView):
    
    
    
    # GET: List all active orders
    def get(self, request):
        orders = Order.objects.filter(is_active=True)
        serializer = ActiveOrderSerializer(orders, many=True)
        return Response(serializer.data)

    # PATCH: Edit a specific order (e.g., change status)
    def patch(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
            serializer = ActiveOrderSerializer(order, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)