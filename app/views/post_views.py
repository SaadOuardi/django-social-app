from rest_framework.viewsets import ModelViewSet
from app.models.post import Post
from app.serializers.post_serializer import PostSerializer

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
