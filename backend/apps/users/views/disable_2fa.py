from rest_framework.views import APIView
from rest_framework.response import Response

class Disable2FAView(APIView):
    def post(self, request):
        user = request.user
        profile = user.profile

        profile.mfa_enabled = False
        profile.mfa_method = None
        profile.mfa_secret = None

        profile.save()

        return Response({"message": "2FA disabled"})