from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.utils import timezone


class VerifyMFAView(APIView):

    def post(self, request):

        username = request.data.get("username")
        code = request.data.get("code")

        try:
            user = User.objects.get(
                username=username
            )

        except User.DoesNotExist:

            return Response({
                "message": "User not found"
            }, status=404)

        profile = user.profile

        # Check code
        if profile.mfa_code != code:

            return Response({
                "message": "Invalid code"
            }, status=400)

        # Check expiration
        if timezone.now() > profile.mfa_expiry:

            return Response({
                "message": "Code expired"
            }, status=400)

        request.session["mfa_verified"] = True

        return Response({
            "message": "MFA verified"
        })