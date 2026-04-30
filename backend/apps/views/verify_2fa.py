from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login
from apps.models import User
from apps.utils.twofa import get_totp

class Verify2FAView(APIView):
    def post(self, request):
        code = request.data.get("code")
        user_id = request.session.get("user_id")

        if not user_id:
            return Response({"success": False, "error": "Session expired"})

        user = User.objects.get(id=user_id)

        # ✅ TOTP
        if user.twofa_method == "totp":
            totp = get_totp(user.twofa_secret)
            if totp.verify(code):
                login(request, user)
                return Response({"success": True})

        # ✅ SMS
        if user.twofa_method == "sms":
            if code == request.session.get("sms_code"):
                login(request, user)
                return Response({"success": True})

        return Response({"success": False})