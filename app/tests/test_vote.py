from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from app.models.post import Post
from app.models.vote import Vote

User = get_user_model()

class VoteTests(APITestCase):
    def setUp(self):
        """Set up a test user, post, and authentication."""
        self.user = User.objects.create_user(email="testuser@example.com", username="testuser", password="testpassword")
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(title="Test Post", content="Test Content", owner=self.user)
        self.vote_url = f"/api/votes/{self.post.id}/"

    def test_vote_post(self):
        """Ensure a user can vote on a post."""
        response = self.client.post(self.vote_url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vote.objects.count(), 1)

    def test_remove_vote(self):
        """Ensure a user can remove their vote."""
        Vote.objects.create(user=self.user, post=self.post)
        response = self.client.post(self.vote_url)  # Second call should remove the vote
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Vote.objects.count(), 0)

    def test_vote_on_nonexistent_post(self):
        """Ensure voting on a nonexistent post returns 404."""
        response = self.client.post("/api/votes/00000000-0000-0000-0000-000000000000/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
