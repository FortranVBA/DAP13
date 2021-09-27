"""Project OC DAP 13 - Lettings test file."""

from django.urls import reverse
from django.test import TestCase


class LettingsTests(TestCase):
    """Lettings test case."""

    fixtures = [
        "address_data.json",
        "lettings_data.json"
        ]

    def test_lettings_main(self):
        """Test a successful authentification."""

        url = reverse('lettings_index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"lettingname", response.content)
        self.assertIn(b"londonletting", response.content)

    def test_letting_details(self):
        """Test the user details retrieve as a management team member."""

        url = reverse('letting', args=[2])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Example Street", response.content)
        self.assertIn(b"London", response.content)
        self.assertIn(b"LO", response.content)
        self.assertIn(b"20000", response.content)
