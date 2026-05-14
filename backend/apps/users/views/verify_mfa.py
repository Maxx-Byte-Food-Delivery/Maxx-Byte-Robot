from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login
from apps.utils.twofa import get_totp
from rest_framework.permissions import IsAuthenticated


class VerifyMFAView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        code = request.data.get("code")
        user = request.user
        profile = user.profile

        # 🔐 TOTP
        if profile.mfa_method == "totp":
            totp = get_totp(profile.mfa_secret)

            if not totp.verify(code, valid_window=1):
                return Response({"message": "Invalid code"}, status=400)

        # 📱 SMS
        elif profile.mfa_method == "sms":
            if profile.mfa_code != code:
                return Response({"message": "Invalid code"},status=400)
        else:
            return Response({"message": "No valid MFA method configured"}, status=400)

        login(request, user)
        return Response({
            "message": "MFA verified",
            "role": "staff" if user.is_staff else "student"
        })