import qrcode
import base64
from io import BytesIO
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from apps.utils.twofa import generate_secret, get_provisioning_uri


class SetupTOTPView(APIView):

    def post(self, request):

        user = request.user

        # 🔐 generate secret
        secret = generate_secret()

        # save temporarily (not enabled yet)
        profile = user.profile
        profile.mfa_secret = secret
        profile.save()

        # 📱 create QR URI
        uri = get_provisioning_uri(user, secret)

        # 🧾 generate QR image
        qr = qrcode.make(uri)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")

        # encode to base64
        qr_base64 = base64.b64encode(buffer.getvalue()).decode()

        return Response({
            "qr_code": qr_base64,
            "secret": secret  # optional fallback
        })