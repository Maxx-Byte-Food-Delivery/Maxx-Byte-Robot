import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

stripe.api_key = "sk_test_YOUR_SECRET_KEY_HERE"

class CreateCheckoutSessionView(APIView):

    def post(self, request):
        try:
            cart = request.data.get("cart", [])

            line_items = []
            for item in cart:
                line_items.append({
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": item["name"],
                        },
                        "unit_amount": int(item["price"] * 100),  # Stripe uses cents
                    },
                    "quantity": item["quantity"],
                })

            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=line_items,
                mode="payment",
                success_url="http://localhost:5173/orders",
                cancel_url="http://localhost:5173/checkout",
            )

            return Response({"sessionId": session.id})

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)