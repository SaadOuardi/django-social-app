from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserSerializer

class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
