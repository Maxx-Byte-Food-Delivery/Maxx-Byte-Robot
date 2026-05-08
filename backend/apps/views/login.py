from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from apps.utils.send_sms import send_mfa_code
from apps.utils.twofa import generate_sms_code
from django.contrib.auth.hashers import check_password
from rest_framework import status

class LoginView(APIView):

    def post(self, request):
        
        print("HIT LOGIN VIEW")

        username = request.data.get("username")
        password = request.data.get("password")

        print("USERNAME:", username)
        print("PASSWORD:", password)

        user = authenticate(request, username=username, password=password)

        print("AUTHENTICATE RESULT:", user)

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
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        #Test
        print("USERNAME:", username)
        print("PASSWORD:", password)