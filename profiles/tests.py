from django.urls import reverse
from django.test import TestCase


class ProfilesTests(TestCase):
    """Lettings test case."""

    fixtures = [
        "users_data.json",
        "profiles_data.json"
        ]

    def test_profiles_main(self):
        """Test a successful authentification."""

        url = reverse('profiles_index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"phoareau", response.content)
        self.assertIn(b"phenry", response.content)

    def test_profile_details(self):
        """Test the user details retrieve as a management team member."""

        url = reverse('profile', args=["phenry"])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"phenry", response.content)
        self.assertIn(b"First name: Pierre", response.content)
        self.assertIn(b"Last name: Henry", response.content)
        self.assertIn(b"Email: pihe@mail.com", response.content)
        self.assertIn(b"Favorite city: Paris", response.content)
