# app/services/user_service.py

from rest_framework import status
from rest_framework.response import Response
from app.serializers.user_serializer import UserSerializer

class UserService:
    @staticmethod
    def register_user(request):
        """
        Handles the logic to register a new user.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
