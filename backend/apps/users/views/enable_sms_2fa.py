from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.utils.send_sms import send_mfa_code


class EnableSMS2FAView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        profile = user.profile

        phone_number = request.data.get("phone_number")

        # 📱 Set phone number ONLY when enabling SMS
        if phone_number:
            profile.phone_number = phone_number
            profile.save()

        if not profile.phone_number:
            return Response({
                "message": "Phone number required for SMS MFA"
            }, status=400)

        send_mfa_code(user)

        return Response({
            "message": "Code sent",
            "next": "verify-sms"
        })