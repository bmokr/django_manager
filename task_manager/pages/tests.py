from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pages.views import index, about, login, register


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_about_url_is_resolved(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        resolved_func = resolve(url).func
        self.assertEqual(resolved_func.__name__, 'login')

    def test_register_url_is_resolved(self):
        url = reverse('register')
        resolved_func = resolve(url).func
        self.assertEqual(resolved_func.__name__, 'register')
