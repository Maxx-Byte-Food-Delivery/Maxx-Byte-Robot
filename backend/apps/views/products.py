from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.models.product import Product

@api_view(['GET'])
def get_all_products(request):
    return Response({"products": Product.objects.all().values()})