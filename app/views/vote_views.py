# app/views/vote_views.py

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from app.services.vote_service import VoteService

class VoteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        return VoteService.toggle_vote(request, post_id)

    def get(self, request, post_id):
        return VoteService.get_vote_count(request, post_id)
