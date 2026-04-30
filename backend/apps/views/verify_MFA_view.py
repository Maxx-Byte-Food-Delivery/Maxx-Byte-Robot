from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils import timezone
from apps.utils.twofa import get_totp



class VerifyMFAView(APIView):

    def post(self, request):

        code = request.data.get("code")
        user_id = request.session.get("user_id")


        if not user_id:
            return Response({
                "message": "Session expired"
            }, status=400)


        try:
            user = User.objects.get(id=user_id)

        except User.DoesNotExist:

            return Response({
                "message": "User not found"
            }, status=404)

        profile = user.profile

        #TOTP
        if profile.mfa_method == "totp":
            totp = get_totp(profile.nfa_secret)

            if not totp.verify(code):
                return Response({
                    "message": "Invalid code"
                }, status=400)
        
        #SMS
        elif profile.mfa_method == "sms":
            

            # Check code
            if profile.mfa_code != code:
                return Response({
                    "message": "Invalid code"
                }, status=400)
            
            if timezone.now() > profile.mfa_expiry:
                return Response({
                    "message": "Code expired"
                }, status = 400)

        login(request, user)

        request.session.pop("user_id", None)
        request.session.pop("sms_code", None)

        return Response({
            "message": "MFA verified",
            "role": "staff" if user.is_staff else "student"
        })