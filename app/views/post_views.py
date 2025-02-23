# app/views/post_views.py

from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from app.services.post_service import PostService

class PostViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        return PostService.list_create_posts(request)

    def create(self, request):
        return PostService.list_create_posts(request)

    def retrieve(self, request, pk=None):
        return PostService.retrieve_update_destroy(request, pk)

    def update(self, request, pk=None):
        return PostService.retrieve_update_destroy(request, pk)

    def partial_update(self, request, pk=None):
        return PostService.retrieve_update_destroy(request, pk)

    def destroy(self, request, pk=None):
        return PostService.retrieve_update_destroy(request, pk)
