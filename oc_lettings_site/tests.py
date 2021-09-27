from django.urls import reverse
from django.test import TestCase


class IndexTests(TestCase):
    """Lettings test case."""

    def test_index(self):
        """Test a successful authentification."""

        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Profiles", response.content)
        self.assertIn(b"Lettings", response.content)

