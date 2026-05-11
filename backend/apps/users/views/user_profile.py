from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserProfileView(APIView):
    def get(self, request):

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