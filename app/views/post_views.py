from rest_framework.viewsets import ModelViewSet
from app.models.post import Post
from app.serializers.post_serializer import PostSerializer
from rest_framework.permissions import IsAuthenticated

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
