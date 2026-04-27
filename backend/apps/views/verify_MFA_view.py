from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from django_otp import devices_for_user


class VerifyMFAView(APIView):

    def post(self, request):

        username = request.data.get("username")
        token = request.data.get("token")

        try:
            user = User.objects.get(
                username=username
            )

        except User.DoesNotExist:

            return Response({
                "message": "User not found"
            }, status=404)

        device = devices_for_user(user).first()

        if device and device.verify_token(token):

            return Response({
                "message": "MFA verified"
            })

        return Response({
            "message": "Invalid MFA code"
        }, status=400)