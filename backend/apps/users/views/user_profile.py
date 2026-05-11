from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserProfileView(APIView):

    permission_classes = [IsAuthenticated]

    # 📖 GET user profile
    def get(self, request):
        profile = request.user.profile

        return Response({
            "username": request.user.username,
            "role": profile.role,

            # 🔐 MFA settings
            "mfa_enabled": profile.mfa_enabled,
            "mfa_method": profile.mfa_method,

            # 📱 IMPORTANT for SMS MFA
            "phone_number": profile.phone_number,
        })
    # ✏️ UPDATE profile settings
    def patch(self, request):
        profile = request.user.profile

        phone_number = request.data.get("phone_number")
        mfa_method = request.data.get("mfa_method")

        # 📱 Update phone number
        if phone_number is not None:
            profile.phone_number = phone_number

        # 🔐 Update MFA method
        if mfa_method in ["sms", "totp"]:
            profile.mfa_method = mfa_method

        profile.save()

        return Response({
            "message": "Profile updated",
            "phone_number": profile.phone_number,
            "mfa_method": profile.mfa_method
        })