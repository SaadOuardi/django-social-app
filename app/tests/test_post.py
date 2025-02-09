from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from app.models.post import Post

User = get_user_model()

class PostTests(APITestCase):
    def setUp(self):
        """Set up a test user and authentication token."""
        self.user = User.objects.create_user(email="testuser@example.com", username="testuser", password="testpassword")
        self.client.force_authenticate(user=self.user)
        self.post_url = "/api/posts/"

    # def test_create_post(self):
    #     """Ensure an authenticated user can create a post."""
    #     data = {
    #         "title": "Test Post",
    #         "content": "This is a test post content",
    #         "published": True
    #     }
    #     response = self.client.post(self.post_url, data, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Post.objects.count(), 1)
    #     self.assertEqual(Post.objects.get().title, "Test Post")

    def test_get_posts(self):
        """Ensure we can retrieve a list of posts."""
        Post.objects.create(title="Test Post", content="Test Content", owner=self.user)
        response = self.client.get(self.post_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_post(self):
        """Ensure we can retrieve a single post by ID."""
        post = Post.objects.create(title="Test Post", content="Test Content", owner=self.user)
        response = self.client.get(f"/api/posts/{post.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Post")
        
# add failing tests
