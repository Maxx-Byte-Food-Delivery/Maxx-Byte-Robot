from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET","POST"])
def logout_view(request):
    if not request.user.is_authenticated:
        return Response({ 
            "success": False, 
            "message": "You are not logged in" 
            }, status=status.HTTP_401_UNAUTHORIZED)
    logout(request)

    return Response({
        "success": True,
        "message": "Logged out successfully"
    })