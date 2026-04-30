from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from apps.models.order import Order
from apps.models.product import Product
from apps.models.order_item import OrderItem


@api_view(['GET'])
def View_History(request, user_id):
    if request.user.id != user_id:
        return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)
    
    orders = Order.objects.filter(user_id=user_id)

    item_query = request.GET.get('item')
    date_query = request.GET.get('date')

    if item_query:
        orders = orders.filter(order_items__product__name__icontains=item_query)

    if date_query:
        orders = orders.filter(created_at__date=date_query)

    orders = orders.distinct()
    order_list = list(orders.values('id', 'total_price', 'status', 'user', 'created_at'))

    return Response(order_list)


@api_view(['GET'])
def item(request, user_id, id):
    if request.user.id != user_id:
        return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)
    
    try:
        order = Order.objects.get(id=id, user_id=user_id)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

    order_items = []
    for item in order.order_items.select_related('product').all():
        order_items.append({
            'id': item.id,
            'product': {
                'id': item.product.id if item.product else None,
                'name': item.product.name if item.product else None,
                'price': item.product.price if item.product else None,
            },
            'quantity': item.quantity,
            'price': item.price,
        })

    return Response({
        'order': {
            'id': order.id,
            'total_price': order.total_price,
            'status': order.status,
            'created_at': order.created_at,
            'user': order.user.id if order.user else None,
        },
        'order_items': order_items,
    })


def reorder(request, user_id, id):
    try:
        old_Order = Order.objects.get(id=id, user_id=user_id)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
    
    new_Order = Order.objects.create(total_price=old_Order.total_price, user_id=user_id)

    for item in old_Order.order_items.all():
        OrderItem.objects.create(order=new_Order, product=item.product, quantity=item.quantity)

    return redirect('view_history_item', id=new_Order.id)