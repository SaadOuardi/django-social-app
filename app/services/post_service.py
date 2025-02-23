# app/services/post_service.py

from rest_framework import status
from rest_framework.response import Response
from app.models.post import Post
from app.serializers.post_serializer import PostSerializer

class PostService:
    @staticmethod
    def list_create_posts(request):
        """
        If GET: Return a list of posts.
        If POST: Create a new post (automatically sets the request.user as owner).
        """
        if request.method == "GET":
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == "POST":
            serializer = PostSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                # Automatically set the owner from the authenticated user
                serializer.save(owner=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def retrieve_update_destroy(request, pk):
        """
        For GET, PUT/PATCH, DELETE operations on a single post.
        """
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        # For GET request:
        if request.method == "GET":
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # For update (PUT/PATCH)
        if request.method in ["PUT", "PATCH"]:
            # Check ownership
            if request.user != post.owner:
                return Response({"error": "Not authorized to update this post"}, status=status.HTTP_403_FORBIDDEN)
            serializer = PostSerializer(post, data=request.data, partial=(request.method == "PATCH"), context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # For DELETE request:
        if request.method == "DELETE":
            if request.user != post.owner:
                return Response({"error": "Not authorized to delete this post"}, status=status.HTTP_403_FORBIDDEN)
            post.delete()
            return Response({"message": "Post deleted"}, status=status.HTTP_204_NO_CONTENT)
