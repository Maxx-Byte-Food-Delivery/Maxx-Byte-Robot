from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from apps.models.active_order import ActiveOrder
from apps.serializers.active_order import ActiveOrderSerializer


@api_view(["GET", "PUT", "PATCH"])
def active_order_detail(request, pk):
    try:
        order = ActiveOrder.objects.get(pk=pk)
    except ActiveOrder.DoesNotExist:
        return Response(
            {"detail": "Order not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    # GET request → return order
    if request.method == "GET":
        serializer = ActiveOrderSerializer(order)
        return Response(serializer.data)

    # UPDATE request → validate editing rules
    if not order.can_edit():
        return Response(
            {"detail": "Order cannot be edited after dispatch stage"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = ActiveOrderSerializer(
        order,
        data=request.data,
        partial=(request.method == "PATCH")
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)