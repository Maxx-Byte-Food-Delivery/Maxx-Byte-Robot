from django.contrib.auth.models import User
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

class LoginView(APIView):

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")
        user_type = request.data.get("user_type")
        user = authenticate(username=username, password=password)

        print("USERNAME:", username)
        print("PASSWORD:", password)

        if user is None:
            return Response({
                "message": "Invalid credentials"
            }, status=400)

        # Staff login check
        if user_type == "staff" and not user.is_staff:
            return Response({
                "message": "Not a staff account"
            }, status=403)

        # Student login check
        if user_type == "student" and user.is_staff:
            return Response({
                "message": "Not a student account"
            }, status=403)

        return Response({
            "message": "Login successful",
            "user_type": "staff" if user.is_staff else "student"
        })
