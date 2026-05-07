from rest_framework.views import APIView
from rest_framework.response import Response
from apps.products.models.product import Product

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        return Response({"products": Product.objects.all().values()})