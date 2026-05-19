from rest_framework.response import Response
from rest_framework import status
from apps.orders.models import Order
from apps.orders.serializers.active_order import ActiveOrderSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def active_order(request, order_id):
    if not request.user.is_authenticated:
        return Response({'detail': 'You must be logged in to track an order'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        order = Order.objects.get(id=order_id, user=request.user, status="active")
    except Order.DoesNotExist:
        return Response({'error': 'Active order not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ActiveOrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def active_orders(request):
    # 1. Enforce Authentication Context
    if not request.user.is_authenticated:
        return Response({'detail': 'You must be logged in to track orders'}, status=status.HTTP_401_UNAUTHORIZED)

    orders = Order.objects.filter(user=request.user, status="active").distinct()
    
    if not orders.exists():
        return Response({'message': "No Active Orders"}, status=status.HTTP_200_OK)

    # 3. Serialize and return the records list array
    serializer = ActiveOrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PATCH'])
def patch_order(request, order_id):
    # 1. Enforce Authentication Context
    if not request.user.is_authenticated:
        return Response({'detail': 'You must be logged in to update an order'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        # 2. FIXED: Retrieve single target order owned by the session user
        order = Order.objects.get(id=order_id, user=request.user)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

    # 3. Perform partial validation and updates
    serializer = ActiveOrderSerializer(order, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)