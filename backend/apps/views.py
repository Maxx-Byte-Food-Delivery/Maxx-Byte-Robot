from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order

@api_view(['GET', 'POST'])

def hello_world(request):
    return Response({"message": "Hello World!"})

def login_view(request):
    username = request.data.get("username")
    password = request.POST("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        return Response({
            "success": True,
            "message": "Login Sucessful",
            "username": user.username
        })
    else:
        return Response({
            "success": False,
            "message": "Invalid Login"},
            status=status.HTTP_401_UNAUTHORIZED
        )

@login_required
def order_history(request):
    # Filter orders for the logged-in user [3]
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    context = {'orders': orders}
    return render(request, 'order_history.html', context)
    