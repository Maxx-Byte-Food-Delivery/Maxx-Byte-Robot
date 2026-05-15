from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated

from apps.utils.twofa import get_totp


class VerifyMFAView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        code = request.data.get("code")
        user = request.user
        profile = user.profile

        if not code:
            return Response({"message": "Code is required"}, status=400)

        # =========================
        # 🔐 TOTP VERIFICATION
        # =========================
        if profile.mfa_method == "totp":

            totp = get_totp(profile.mfa_secret)

            if not totp.verify(code, valid_window=1):
                return Response({"message": "Invalid code"}, status=400)

        # =========================
        # 📱 SMS VERIFICATION
        # =========================
        elif profile.mfa_method == "sms":

            # check existence
            if not profile.mfa_code:
                return Response({"message": "No MFA code found"}, status=400)

            # check expiry
            if profile.mfa_expiry and timezone.now() > profile.mfa_expiry:
                profile.mfa_code = None
                profile.mfa_expiry = None
                profile.save()

                return Response({"message": "Code expired"}, status=400)

            # check match
            if str(profile.mfa_code) != str(code):
                return Response({"message": "Invalid code"}, status=400)

            # 🔥 IMPORTANT: clear code after success
            profile.mfa_code = None
            profile.mfa_expiry = None
            profile.save()

        else:
            return Response(
                {"message": "No valid MFA method configured"},
                status=400
            )

        # =========================
        # ✅ FINAL LOGIN
        # =========================
        login(request, user)

        return Response({
            "message": "MFA verified",
            "role": "staff" if user.is_staff else "student"
        })