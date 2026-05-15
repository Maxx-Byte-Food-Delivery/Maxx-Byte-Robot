from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.utils.send_sms import send_mfa_code


class ResendMFAView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        user = request.user
        profile = user.profile

        if profile.mfa_method != "sms":
            return Response({
                "message": "SMS MFA not enabled"
            }, status=400)

        # 📩 regenerate + resend
        send_mfa_code(user)

        return Response({
            "message": "Code resent"
        })