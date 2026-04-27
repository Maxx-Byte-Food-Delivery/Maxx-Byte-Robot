from backend.apps.models.users import User
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.models.order import Order
from django.contrib.auth.hashers import check_password

@api_view(['GET', 'POST'])

def hello_world(request):
    return Response({"message": "Hello World!"})