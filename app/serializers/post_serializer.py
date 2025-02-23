from rest_framework import serializers
from app.models.post import Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.id")  # ✅ Make owner read-only

    class Meta:
        model = Post
        fields = ["id", "title", "content", "owner", "created_at"]
