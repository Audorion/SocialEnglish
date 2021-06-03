from django.contrib.auth.models import User
from django.test import Client, TestCase
from .models import Post


class TestIndexPage(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_index_available(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class TestGroups(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_page_not_found(self):
        response = self.client.get('/group/not_exist/')
        self.assertEqual(response.status_code, 404)
