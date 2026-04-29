import stripe
from django.conf import settings
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.models.order import Order
from apps.models.payment import Payment

stripe_api_key = settings.STRIPE_API_KEY

@api_view(['POST'])
def create_checkout_session(request, order_id=None):
    data = request.data if hasattr(request, 'data') else {}
    order_id = order_id or data.get('order')

    if not order_id:
        return Response({'error': 'order_id is required'}, status=400)

    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=404)

    amount = data.get('total_price', order.total_price)
    status = data.get('status', 'pending')
    method = data.get('method', 'card')

    if stripe_api_key:
        stripe.api_key = stripe_api_key
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Food Order',
                    },
                    'unit_amount': int(order.total_price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:3000/success',
            cancel_url='http://localhost:3000/cancel',
            metadata={'order_id': str(order.id)},
        )
        transaction_id = session.id
    else:
        transaction_id = 'test_session'
        session = type('T', (), {'id': transaction_id})()

    Payment.objects.create(
        order=order,
        method=method,
        amount=amount,
        transaction_id=transaction_id,
        status=status,
    )

    return Response({'id': session.id})

def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = settings.STRIPE_API_KEY

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        order_id = session['metadata']['order_id']
        order = Order.objects.get(id=order_id)

        order.status = 'confirmed'
        order.save()

        return HttpResponse(status=200)