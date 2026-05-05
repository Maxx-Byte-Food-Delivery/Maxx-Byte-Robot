from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.utils.send_sms import send_mfa_code


class EnableSMS2FAView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        profile = user.profile

        # 🔁 Prevent overwriting active code (optional but recommended)
        if profile.mfa_code:
            print("Reusing existing code:", profile.mfa_code)
        else:
            send_mfa_code(user)  # ✅ this generates + saves + sends

        return Response({
            "message": "Code sent",
            "next": "verify-sms"
        })