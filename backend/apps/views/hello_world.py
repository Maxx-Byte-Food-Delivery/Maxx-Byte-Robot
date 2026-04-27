
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.models.order import Order
from django.contrib.auth.hashers import check_password

@api_view(['GET', 'POST'])

def hello_world(request):
    return Response({"message": "Hello World!"})