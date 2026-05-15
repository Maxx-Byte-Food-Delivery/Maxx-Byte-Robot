from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.utils.send_sms import send_mfa_code
from apps.users.services.mfa import get_mfa_phone



class EnableSMS2FAView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        user = request.user
        profile = user.profile

        # 📲 THIS is what frontend sends
        phone_number = request.data.get("phone_number")

        # =========================
        # VALIDATION
        # =========================
        if not phone_number:
            return Response({
                "message": "Phone number required"
            }, status=400)

        # =========================
        # SAVE MFA PHONE (NOT SIS PHONE)
        # =========================
        profile.mfa_phone_number = phone_number

        # Optional: only set SIS phone if it was empty
        if not profile.phone_number:
            profile.phone_number = phone_number

        # =========================
        # ENABLE MFA
        # =========================
        profile.mfa_method = "sms"
        profile.mfa_enabled = True
        profile.save()

        # =========================
        # SEND SMS TO SELECTED NUMBER
        # =========================
        send_mfa_code(user)

        return Response({
            "message": "SMS MFA enabled"
        })