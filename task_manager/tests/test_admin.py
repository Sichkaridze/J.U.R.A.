from django.contrib.auth import get_user_model
from django.test import TestCase


class AdminAccessTest(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(username='admin', password='adminpass')
        self.client.login(username='admin', password='adminpass')

    def test_admin_access(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Site administration')