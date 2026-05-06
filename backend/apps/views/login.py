from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from apps.utils.send_sms import send_mfa_code
from apps.utils.twofa import generate_sms_code
from django.contrib.auth.hashers import check_password
from rest_framework import status

class LoginView(APIView):

    def post(self, request):
        print("HIT LOGIN VIEW")   # 👈 add this

        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        profile = user.profile

        # 🔐 STORE USER IN SESSION (for verification step)
        request.session['user_id'] = user.id

        # ======================
        # 👩‍💼 STAFF (MFA REQUIRED)
        # ======================
        if user.is_staff:
            if profile.mfa_method == "totp":
                return Response({
                    "requires_2fa": True,
                    "method": "totp",
                    "role": "staff"
                })
            if profile.mfa_method == "sms":
                send_mfa_code(user)
                request.session['sms_code'] = user.profile.mfa_code
                return Response({
                    "requires_2fa": True,
                    "method": "sms",
                    "role": "staff"
                })
            return Response(
                {"error": "MFA method not configured for staff"},
                status=status.HTTP_400_BAD_REQUEST
            )

        elif profile.role == "student":
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
                    send_mfa_code(user)  # ✅ single source of truth
                    request.session['sms_code'] = user.profile.mfa_code

                    return Response({
                        "requires_2fa": True,
                        "method": "sms",
                        "role": "student"
                    })

                # if enabled but method not recognized, login
                from django.contrib.auth import login
                login(request, user)

                return Response({
                    "requires_2fa": False,
                    "role": "student"
                })

            else:
                # not enabled, login
                from django.contrib.auth import login
                login(request, user)

                return Response({
                    "requires_2fa": False,
                    "role": "student"
                })

        #Test
        print("USERNAME:", username)
        print("PASSWORD:", password)
        print("USER:", user)

        