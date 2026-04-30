from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from apps.utils.send_sms import send_mfa_code
from apps.utils.twofa import generate_sms_code

class LoginView(APIView):

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response({
                "message": "Invalid credentials"
            }, status=400)

        profile = user.profile

        # 🔐 STORE USER IN SESSION (for verification step)
        request.session['user_id'] = user.id

        # ======================
        # 👩‍💼 STAFF (MFA REQUIRED)
        # ======================
        if user.is_staff:

            code = generate_sms_code()
            request.session['sms_code'] = code

            send_mfa_code(user)  # you already have this

            return Response({
                "requires_2fa": True,
                "method": "sms",
                "role": "staff"
            })

        # ======================
        # 👨‍🎓 STUDENT (2FA OPTIONAL)
        # ======================
        if profile.mfa_enabled:

            # 📱 TOTP (Authenticator App)
            if profile.mfa_method == "totp":
                return Response({
                    "requires_2fa": True,
                    "method": "totp",
                    "role": "student"
                })

            # 📩 SMS
            if profile.mfa_method == "sms":
                code = generate_sms_code()
                request.session['sms_code'] = code

                send_mfa_code(user)

                return Response({
                    "requires_2fa": True,
                    "method": "sms",
                    "role": "student"
                })

        # ======================
        # ✅ NO 2FA → LOGIN
        # ======================
        from django.contrib.auth import login
        login(request, user)

        return Response({
            "requires_2fa": False,
            "role": "student"
        })