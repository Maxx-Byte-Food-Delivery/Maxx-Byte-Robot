from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login
from django.utils import timezone

from apps.utils.twofa import get_totp



class VerifyMFAView(APIView):
    permission_classes = []

    def post(self, request):
        user_id = request.session.get("user_id")
        if not user_id:
            return Response({
                "message": "Session expired"
            }, status=401)

        user = User.objects.get(id=user_id)
        profile = user.profile
        code = request.data.get("code")
        
        # FIX: Explicitly check for None or empty string so 0 or "000000" passes
        if code is None or str(code).strip() == "":
            return Response({"message": "Code is required"}, status=400)

        # Ensure code is handled consistently as a string
        code_str = str(code).strip()

        # =========================
        # 🔑 TOTP VERIFICATION
        # =========================
        if profile.mfa_method == "totp":
            totp = get_totp(profile.mfa_secret)
            if not totp.verify(code_str, valid_window=1):
                return Response({"message": "Invalid code"}, status=400)

        # =========================
        # 📱 SMS VERIFICATION
        # =========================
        elif profile.mfa_method == "sms":
            if not profile.mfa_code:
                return Response({"message": "No MFA code found"}, status=400)

            if profile.mfa_expiry and timezone.now() > profile.mfa_expiry:
                profile.mfa_code = None
                profile.mfa_expiry = None
                profile.save()
                return Response({"message": "Code expired"}, status=400)

            if str(profile.mfa_code).strip() != code_str:
                return Response({"message": "Invalid code"}, status=400)

            profile.mfa_code = None
            profile.mfa_expiry = None
            profile.save()
        else:
            return Response(
                {"message": "No valid MFA method configured"}, status=400
            )

        # =========================
        # ✅ FINAL LOGIN
        # =========================
        request.session.pop("user_id", None)
        login(request, user)
        return Response({
            "message": "MFA verified",
            "role": "staff" if user.is_staff else "student"
        })