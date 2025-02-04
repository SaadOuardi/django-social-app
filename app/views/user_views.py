from rest_framework.generics import CreateAPIView
from app.models.user import User
from app.serializers.user_serializer import UserSerializer

class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
