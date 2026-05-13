from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.orders.models import Order
from apps.serializers.active_order import ActiveOrderSerializer

@api_view(['GET'])
def active_order(request, user_id, order_id):
    if not request.user.is_authenticated:
        return Response({'detail': 'You must be logged in to track an order', 'orders': []}, status=status.HTTP_403_FORBIDDEN)
    elif request.user.id != user_id:
        return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)

    orders = Order.objects.filter(user_id=user_id, status = "active")
    if not orders.exists():
        return Response({'error': 'No orders found', 'orders': []}, status=status.HTTP_404_NOT_FOUND)
    orders = orders.distinct()

    order_list = list(orders.values('id', 'total_price', 'status', 'user', 'created_at'))

    serializer = ActiveOrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def active_orders(request, user_id):
    if not request.user.is_authenticated:
        return Response({'detail': 'You must be logged in to track an order', 'orders': []}, status=status.HTTP_403_FORBIDDEN)
    elif request.user.id != user_id:
        return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)

    orders = Order.objects.filter(user_id=user_id, status="active").distinct()
    if not orders.exists():
        return Response({'error': 'No orders found', 'orders': []}, status=status.HTTP_404_NOT_FOUND)

    serializer = ActiveOrderSerializer(orders, many=True)
    return Response(serializer.data)


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