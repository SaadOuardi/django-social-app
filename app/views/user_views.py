from rest_framework.views import APIView
from app.services.user_service import UserService

class UserRegisterView(APIView):
    """
    API view to register new users.
    """
    def post(self, request):
        return UserService.register_user(request)
