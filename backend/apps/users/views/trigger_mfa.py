from rest_framework.views import APIView
from rest_framework.response import Response
from apps.utils.send_sms import send_mfa_code
from apps.utils.twofa import get_totp


class MFATriggerView(APIView):

    def post(self, request):
        user = request.user
        profile = user.profile

        # 📱 SMS flow
        if profile.mfa_method == "sms":
            send_mfa_code(user)
            return Response({"message": "SMS code sent"})

        # 🔐 TOTP flow (no sending needed)
        if profile.mfa_method == "totp":
            return Response({"message": "Enter authenticator code"})

        return Response({"message": "MFA not configured"}, status=400)