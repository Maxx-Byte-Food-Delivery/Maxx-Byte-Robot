import stripe
from django.http import JsonResponse, HttpResponse
from backend.apps.models import Order

stripe_api_key = "sk_test_51TOiPRIlqypzYkQOgEYx78Gpo7XdtZKgjUOkjL4l1UlqSLNaYWxd6snUw0tjKZoPeOMwdRWeYoaPgq0JOhuEiN7z00jG5RdzGW"

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
        mode='payment',
        success_url='http://localhost:3000/success',
        cancel_url='http://localhost:3000/cancel',
    )

    return JsonResponse({'id': session.id})

def stripe_webhook(request):
    event = stripe.Event.construct_from(...)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        order_id = session['metadata']['order_id']
        order = Order.objects.get(id=order_id)

        order.status = 'confirmed'
        order.save()

        return HttpResponse(status=200)