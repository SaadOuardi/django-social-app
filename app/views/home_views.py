
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(APIView):
    def home(self, request):
        return Response('Hello, World!')