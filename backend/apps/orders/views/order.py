import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.orders.models.order import Order
from apps.orders.models.order_item import OrderItem
from apps.orders.models.cart import Cart

@csrf_exempt
def create_order(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    if not request.user.is_authenticated:
        return JsonResponse({"error": "Login required"}, status=401)

    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        return JsonResponse({"error": "Cart not found"}, status=404)

    cart_items = cart.items.select_related("product").all()
    if not cart_items.exists():
        return JsonResponse({"error": "Cart is empty"}, status=400)

    data = json.loads(request.body)
    shipping = data.get("shipping_address", {})
    address_str = (
        f"{shipping.get('addressLine1')} {shipping.get('addressLine2', '')} "
        f"{shipping.get('city')}, {shipping.get('state')} {shipping.get('zipCode')}"
    ).strip()

    order = Order.objects.create(
        user=request.user,
        address=address_str,
        status='pending'
    )

    for cart_item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=cart_item.product,
            quantity=cart_item.quantity
        )

    return JsonResponse({"order_id": order.id})