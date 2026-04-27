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
        user = authenticate(request, username=username, password=password)

        print("USERNAME:", username)
        print("PASSWORD:", password)

        if user is None:
            return Response({
                "message": "Invalid credentials"
            }, status=400)

        profile = user.profile

        #Determine role automatically
        # Staff → ALWAYS MFA
        if user.is_staff:

            return Response({
                "mfa_required": True,
                "role": "staff"
            })

        # Student → Only if enabled
        if profile.mfa_enabled:

            return Response({
                "mfa_required": True,
                "role": "student"
            })

        # No MFA needed
        return Response({
            "mfa_required": False,
            "role": "student"
        })