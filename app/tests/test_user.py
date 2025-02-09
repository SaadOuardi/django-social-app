from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTests(APITestCase):
    def setUp(self):
        """Set up test data for user-related tests."""
        self.register_url = "/api/users/register/"  # ✅ Update the correct URL
        self.user_data = {
            "email": "testuser@example.com",
            "username": "testuser",
            "password": "testpassword123"
        }

    def test_register_user_api(self):
        """Ensure we can register a new user via API."""
        response = self.client.post(self.register_url, self.user_data, format="json")
        print("🔍 Debug: Response Content =", response.content)  # ✅ Print response details
        print("🔍 Debug: Response Status Code =", response.status_code)  # ✅ Print status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, self.user_data["email"])

    def test_register_user_with_duplicate_email(self):
        """Ensure registration fails if the email is already used."""
        self.client.post(self.register_url, self.user_data, format="json")  # Create a user first
        response = self.client.post(self.register_url, self.user_data, format="json")  # Try again
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Should fail
        self.assertEqual(User.objects.count(), 1)  # Still only one user

    def test_register_user_with_missing_fields(self):
        """Ensure registration fails if required fields are missing."""
        incomplete_data = {
            "email": "missing@example.com"
        }
        response = self.client.post(self.register_url, incomplete_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Should fail
