# app/services/vote_service.py

from rest_framework import status
from rest_framework.response import Response
from app.models.vote import Vote
from app.models.post import Post

class VoteService:
    @staticmethod
    def toggle_vote(request, post_id):
        """
        If the user has already voted on the given post, delete the vote.
        Otherwise, create a new vote.
        """
        user = request.user
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        existing_vote = Vote.objects.filter(user=user, post=post).first()
        if existing_vote:
            existing_vote.delete()
            return Response({"message": "Vote removed"}, status=status.HTTP_200_OK)
        else:
            Vote.objects.create(user=user, post=post)
            return Response({"message": "Vote added"}, status=status.HTTP_201_CREATED)

    @staticmethod
    def get_vote_count(request, post_id):
        """
        Returns the total number of votes for a given post.
        """
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        vote_count = Vote.objects.filter(post=post).count()
        return Response({"post_id": post_id, "total_votes": vote_count}, status=status.HTTP_200_OK)
