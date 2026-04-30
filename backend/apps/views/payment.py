import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from apps.models.order import Order
from apps.models.payment import Payment

stripe.api_key = settings.STRIPE_API_KEY


def create_checkout_session(request, order_id):

    order = Order.objects.get(id=order_id)

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
        metadata={
            "order_id": order.id
        },
        mode='payment',
        success_url='http://localhost:3000/success',
        cancel_url='http://localhost:3000/cancel',
    )

    return JsonResponse({'id': session.id})


def stripe_webhook(request):

    event = stripe.Event.construct_from(request.json, stripe.api_key)

    if event['type'] == 'checkout.session.completed':

        session = event['data']['object']
        order_id = session['metadata']['order_id']

        order = Order.objects.get(id=order_id)
        order.status = 'confirmed'
        order.save()

    return HttpResponse(status=200)