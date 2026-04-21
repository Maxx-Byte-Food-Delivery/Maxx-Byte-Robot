from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework import status

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


    
    