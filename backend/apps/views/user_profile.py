from rest_framework.views import APIView
from rest_framework.response import Response

class UserProfileView(APIView):
    def get(self, request):

        if not request.user.is_authenticated:
            return Response({"error": "Not authenticated"}, status=401)
        
        profile = request.user.profile

        return Response({
            "mfa_enabled": profile.mfa_enabled,
            "mfa_method": profile.mfa_method
        })