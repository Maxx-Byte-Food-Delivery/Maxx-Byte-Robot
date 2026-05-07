from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login
from django.contrib.auth.models import User
from apps.utils.twofa import get_totp

class Verify2FAView(APIView):
    def post(self, request):
        code = request.data.get("code")
        user_id = request.session.get("user_id")

        if not user_id:
            return Response({"success": False, "error": "Session expired"}, status=400)

        user = User.objects.get(id=user_id)
        profile = user.profile

        # ✅ TOTP
        if profile.mfa_method == "totp":
            totp = get_totp(user.mfa_secret)
            if totp.verify(code):
                login(request, user)
                print("USER LOGGED IN:", request.user)
                request.session.pop("user_id", None)
                return Response({
                    "success": True,
                    "role": "staff" if user.is_staff else "student"
                })

        # ✅ SMS
        if profile.mfa_method == "sms":
            
            if code == request.session.get("sms_code"):
                login(request, user)
                print("USER LOGGED IN:", request.user)

                request.session.pop("user_id", None)
                request.session.pop("sms_code", None)
                
                return Response({
                    "success": True,
                    "role": "staff" if user.is_staff else "student",
                })

        return Response({
            "success": False,
            "error": "Invalid code"
        }, status=400)