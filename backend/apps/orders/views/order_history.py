from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from apps.orders.models.order import Order
from apps.products.models.product import Product
from apps.orders.models.order_item import OrderItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.orders.models import Order  # Adjust this import to match your model location

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def View_History(request):
    # 1. Verify Authentication Context
    if not request.user.is_authenticated:
        return Response({
            'error': 'You must be logged in to view order history', 
            'orders': []
        }, status=status.HTTP_401_UNAUTHORIZED)

    orders = Order.objects.filter(user=request.user).order_by('updated_at')
    
    if not orders.exists():
        return Response([], status=status.HTTP_200_OK)

    item_query = request.GET.get('item')
    date_query = request.GET.get('date')
    
    if item_query:
        orders = orders.filter(order_items__product__name__icontains=item_query)
    if date_query:
        orders = orders.filter(created_at__date=date_query)
        
    orders = orders.distinct()
    
    order_list = []
    for order in orders:
        order_list.append({
            "id": order.id,
            "total_price": str(order.total_price),
            "status": order.status,
            "user": order.user.id,
            "address": order.address,
            "created_at": order.created_at,
            "updated_at": order.updated_at,
        })

    return Response(order_list, status=status.HTTP_200_OK)


@api_view(['GET'])
def item(request, id):
    # 1. Verify Authentication Context
    if not request.user.is_authenticated:
        return Response({
            'error': 'You must be logged in to view order history',
            'orders': []
        }, status=status.HTTP_401_UNAUTHORIZED)

    try:
        # FIXED: Use .get() instead of .filter() to return a single model instance
        order = Order.objects.get(user=request.user, id=id)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

    # 2. Build the detailed items response payload
    order_items = []
    # This loop works properly now that 'order' is an explicit object instance
    for item in order.order_items.select_related('product').all():
        order_items.append({
            'id': item.id,
            'product_name': item.product.name,
            'price': str(item.product.price),  # Converts Decimal fields safely to strings
            'quantity': item.quantity,
        })

    # 3. Return the populated item list details
    return Response({
        'order_id': order.id,
        'status': order.status,
        'total_price': str(order.total_price),
        'created_at': order.created_at,
        'updated_at': order.updated_at,
        'items': order_items
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
def reorder(request, user_id, id):
    if request.user.id != user_id:
        return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)
    
    try:
        old_Order = Order.objects.get(id=id, user_id=user_id)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
    
    new_Order = Order.objects.create(total_price=old_Order.total_price, user_id=user_id, status="pending")

    for item in old_Order.order_items.all():
        OrderItem.objects.create(order=new_Order, product=item.product, quantity=item.quantity)

    return Response({'message': 'Order reordered successfully', 'new_order_id': new_Order.id})