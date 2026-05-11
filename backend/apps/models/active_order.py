from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def ActiveOrder(request):

    data = [
        {
            "id": 1,
            "customer_name": "John",
            "items": "Burger, Fries",
            "status": "Preparing"
        },
        {
            "id": 2,
            "customer_name": "Sarah",
            "items": "Pizza, Soda",
            "status": "Pending"
        }
    ]

    return Response(data)