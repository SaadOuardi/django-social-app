from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from app.models.vote import Vote
from app.models.post import Post
from app.serializers.vote_serializer import VoteSerializer

class VoteView(APIView):
    """
    API view for users to vote (like/unlike) on a post.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        """
        Allows a user to vote (like) a post.
        If the vote already exists, it removes the vote (unlike).
        """
        user = request.user

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user has already voted on the post
        existing_vote = Vote.objects.filter(user=user, post=post).first()

        if existing_vote:
            # User has already voted → Remove the vote (unlike)
            existing_vote.delete()
            return Response({"message": "Vote removed"}, status=status.HTTP_200_OK)
        else:
            # User has not voted yet → Add vote (like)
            vote = Vote(user=user, post=post)
            vote.save()
            return Response({"message": "Vote added"}, status=status.HTTP_201_CREATED)

    def get(self, request, post_id):
        """
        Returns the total number of votes for a given post.
        """
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        vote_count = Vote.objects.filter(post=post).count()
        return Response({"post_id": post_id, "total_votes": vote_count}, status=status.HTTP_200_OK)
