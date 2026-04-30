from rest_framework.views import APIView
from rest_framework.response import Response

class EnableSMS2FAView(APIView):
    def post(self, request):
        user = request.user
        profile = user.profile

        profile.mfa_enabled = True
        profile.mfa_method = "sms"
        profile.save()

        return Response({"message": "SMS 2FA enabled"})