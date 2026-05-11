from rest_framework.views import APIView
from rest_framework.response import Response
from apps.utils.twofa import get_totp


class ConfirmTOTPView(APIView):

    def post(self, request):

        code = request.data.get("code", "").strip()
        user = request.user
        profile = user.profile

        totp = get_totp(profile.mfa_secret)

        print("SECRET:", profile.mfa_secret)
        print("CODE:", code)
        print("RESULT:", totp.verify(code, valid_window=1))

        if not totp.verify(code, valid_window=1):
            return Response({
                "message": "Invalid code"
            }, status=400)

        # ✅ enable 2FA
        profile.mfa_enabled = True
        profile.mfa_method = "totp"
        profile.save()

        return Response({
            "message": "TOTP enabled"
        })