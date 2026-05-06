from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import timedelta
from apps.utils.send_sms import send_mfa_code


class VerifySMSView(APIView):
    permission_classes = [IsAuthenticated]

    # 🔐 VERIFY CODE
    def post(self, request):
        print("METHOD:", request.method)
        print("DATA:", request.data)

        user = request.user
        profile = user.profile

        code = request.data.get("code", "").strip()

        print("INPUT:", code)
        print("STORED:", profile.mfa_code)

        if not code:
            return Response({"message": "Code required"}, status=400)

        if profile.mfa_expiry and timezone.now() > profile.mfa_expiry:
            return Response({"message": "Code expired"}, status=400)

        if str(profile.mfa_code) != code:
            return Response({"message": "Invalid code"}, status=400)

        # ✅ Success → enable MFA
        profile.mfa_enabled = True
        profile.mfa_method = "sms"

        # 🔒 clear code after use
        profile.mfa_code = None
        profile.mfa_expiry = None
        profile.save()

        return Response({
            "message": "SMS verified",
            "role": "staff" if user.is_staff else "student"
        })

    # 🔁 RESEND CODE
    def get(self, request):
        print("METHOD:", request.method)
        print("DATA:", request.data)

        user = request.user
        profile = user.profile

        # ⏱ Prevent spam (reuse expiry instead of old field)
        if profile.mfa_expiry and profile.mfa_expiry > timezone.now():
            remaining = int((profile.mfa_expiry - timezone.now()).total_seconds())
            if remaining > 240:  # optional cooldown window (~1 min after send)
                return Response(
                    {"message": "Wait before requesting another code"},
                    status=429
                )

        # ✅ Use the SAME function
        send_mfa_code(user)

        return Response({"message": "Code resent"})