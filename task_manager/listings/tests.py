from django.urls import reverse, resolve
from django.test import TestCase
from django.contrib.auth.models import User
from .views import history_view


class YourTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_logged_home_url_resolves(self):
        url = reverse('logged_home')
        resolved_func = resolve(url).func
        self.assertEqual(resolved_func.__name__, 'logged_home')

    def test_listing_url_resolves(self):
        url = reverse('listing', args=[1])
        resolved_func = resolve(url).func
        self.assertEqual(resolved_func.__name__, 'listing')

    def test_history_view_url_resolves(self):
        url = reverse('history_view', args=[1])
        resolved_func = resolve(url).func
        self.assertEqual(resolved_func, history_view)

    def test_change_status_url_resolves(self):
        url = reverse('change_status')
        resolved_func = resolve(url).func
        self.assertEqual(resolved_func.__name__, 'change_status')

    def test_delete_listing_url_resolves(self):
        url = reverse('delete_listing', args=[1])
        resolved_func = resolve(url).func
        self.assertEqual(resolved_func.__name__, 'delete_listing')

    def test_add_new_url_resolves(self):
        url = reverse('add_new')
        resolved_func = resolve(url).func
        self.assertEqual(resolved_func.__name__, 'add_new')

    def test_create_listing_url_resolves(self):
        url = reverse('create_listing')
        resolved_func = resolve(url).func
        self.assertEqual(resolved_func.__name__, 'create_listing')

    def test_edit_listing_page_url_resolves(self):
        url = reverse('edit_listing_page', args=[1])
        resolved_func = resolve(url).func
        self.assertEqual(resolved_func.__name__, 'edit_listing_page')

    def test_edit_url_resolves(self):
        url = reverse('edit')
        resolved_func = resolve(url).func
        self.assertEqual(resolved_func.__name__, 'edit')
