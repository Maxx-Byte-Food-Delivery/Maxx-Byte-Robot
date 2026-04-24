from apps.models.users import User
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.models.orders import Order
from django.contrib.auth.hashers import check_password

@api_view(['GET', 'POST'])

@login_required
def order_history(request):
    # Filter orders for the logged-in user [3]
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    context = {'orders': orders}
    return render(request, 'order_history.html', context)
        
    
    