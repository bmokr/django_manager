from django.test import TestCase
from django.urls import reverse


class AccountsTests(TestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

    def test_register_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)

    def test_register_post_request(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'securepassword',
            'password2': 'securepassword',
        }
        response = self.client.post(self.register_url, data)
        self.assertRedirects(response, reverse('login'))

    def test_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)


