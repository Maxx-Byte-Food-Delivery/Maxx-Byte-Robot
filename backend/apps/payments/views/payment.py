import stripe
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.orders.models.order import Order

@csrf_exempt
def create_checkout_session(request, order_id):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return JsonResponse({"error": "Order not found"}, status=404)

    line_items = [
        {
            "price_data": {
                "currency": "usd",
                "product_data": {"name": item.product.name},
                "unit_amount": int(item.price * 100),
            },
            "quantity": item.quantity,
        }
        for item in order.order_items.all()
    ]

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        success_url=f"http://localhost:5173/order-confirmation/{order.id}/",
        cancel_url="http://localhost:5173/cancel",
    )

    return JsonResponse({"url": session.url})

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    webhook_secret = 'your_stripe_webhook_secret'  # ← move to .env

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
    except (ValueError, stripe.error.SignatureVerificationError):
        return JsonResponse({"error": "Invalid signature"}, status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        order_id = session['success_url'].split('/')[-2]
        try:
            order = Order.objects.get(id=order_id)
            order.status = 'confirmed'
            order.save()
        except Order.DoesNotExist:
            pass

    return JsonResponse({"status": "ok"})