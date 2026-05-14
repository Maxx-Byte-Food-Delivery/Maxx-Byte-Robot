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

        if not profile.phone_number:
            return Response({
                "message": "Phone number required for SMS"
            }, status=400)

        profile.mfa_method = "sms"
        profile.mfa_enabled = True
        profile.save();

        send_mfa_code(user)

        return Response({
            "message": "SMS MFA enabled"
        })