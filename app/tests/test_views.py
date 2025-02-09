from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from app.models.post import Post
from app.models.vote import Vote
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserTests(APITestCase):
    def test_register_user(self):
        """
        Ensure we can register a new user.
        """
        data = {
            "email": "testuser@example.com",
            "username": "testuser",
            "password": "testpassword"
        }
        response = self.client.post("/api/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, "testuser@example.com")


class PostTests(APITestCase):
    def setUp(self):
        """
        Set up a test user and authentication token.
        """
        self.user = User.objects.create_user(email="testuser@example.com", username="testuser", password="testpassword")
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        """
        Ensure an authenticated user can create a post.
        """
        data = {
            "title": "Test Post",
            "content": "This is a test post."
        }
        response = self.client.post("/api/posts/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, "Test Post")

    def test_get_posts(self):
        """
        Ensure we can retrieve a list of posts.
        """
        Post.objects.create(title="Test Post", content="Test Content", owner=self.user)
        response = self.client.get("/api/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class VoteTests(APITestCase):
    def setUp(self):
        """
        Set up a test user, post, and authentication.
        """
        self.user = User.objects.create_user(email="testuser@example.com", username="testuser", password="testpassword")
        self.post = Post.objects.create(title="Test Post", content="Test Content", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_vote_post(self):
        """
        Ensure a user can vote on a post.
        """
        response = self.client.post(f"/api/votes/{self.post.id}/")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vote.objects.count(), 1)

    def test_remove_vote(self):
        """
        Ensure a user can remove their vote.
        """
        Vote.objects.create(user=self.user, post=self.post)
        response = self.client.post(f"/api/votes/{self.post.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Vote.objects.count(), 0)
