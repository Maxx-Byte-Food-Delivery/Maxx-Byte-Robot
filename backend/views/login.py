from backend.apps.models.users import User
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from backend.apps.models.orders import Order
from django.contrib.auth.hashers import check_password

@api_view(['GET', 'POST'])

class LoginView(APIView):

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        print("USERNAME:", username)
        print("PASSWORD:", password)


        try:

            user = User.objects.get(
                username=username
            )
            print("USER FOUND:", user.username)

            if check_password(password,user.password):

                return Response({
                    "message": "Login successful",
                    "username": user.username
                })

            else:

                print("PASSWORD WRONG")

                return Response(
                    {"error": "Wrong password"},
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except User.DoesNotExist:

            print("USER NOT FOUND")

            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )
