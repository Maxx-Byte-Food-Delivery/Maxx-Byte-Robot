from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET","POST"])
def logout_view(request):

    logout(request)

    return Response({
        "success": True,
        "message": "Logged out successfully"
    })