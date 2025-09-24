# api/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username="testuser", password="testpass123")

        # Authenticated client
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass123")

        # Sample books
        self.book1 = Book.objects.create(
            title="Django Basics", author="Alice", publication_year=2020)
        self.book2 = Book.objects.create(
            title="REST API Guide", author="Bob", publication_year=2021)

        self.create_url = reverse("book-create")
        self.list_url = reverse("book-list")
        self.detail_url = lambda pk: reverse("book-detail", args=[pk])
        self.update_url = lambda pk: reverse("book-update", args=[pk])
        self.delete_url = lambda pk: reverse("book-delete", args=[pk])

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        data = {
            "title": "New Book",
            "author": "Charlie",
            "publication_year": 2022
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        self.client.logout()
        data = {
            "title": "Unauthorized Book",
            "author": "Hacker",
            "publication_year": 2023
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        data = {"title": "Updated Django Book"}
        response = self.client.patch(self.update_url(self.book1.pk), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django Book")

    def test_delete_book(self):
        response = self.client.delete(self.delete_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url + "?author=Alice")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Alice")

    def test_search_books(self):
        response = self.client.get(self.list_url + "?search=REST")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "REST API Guide")

    def test_order_books_by_publication_year_desc(self):
        response = self.client.get(
            self.list_url + "?ordering=-publication_year")
        self.assertEqual(response.data[0]["publication_year"], 2021)
