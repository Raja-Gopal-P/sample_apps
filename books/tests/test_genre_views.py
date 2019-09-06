from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Genre
from ..genre_views import GenreCreateView, GenreListView


class GenreCreateViewTest(TestCase):

    def setUp(self):
        self.genre = Genre.objects.create(type='type')
        self.url = reverse('books:books-create-genre')

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, GenreCreateView)

    def test_success_redirect(self):
        genre_type = '{type}_unique'.format(type=self.genre.type)
        response = self.client.post(self.url, data={'type': genre_type, })

        self.assertRedirects(response, reverse('books:books-genre-list'))
        self.assertTrue(Genre.objects.filter(type=genre_type))

    def test_failure_response(self):
        genre_type = self.genre.type
        response = self.client.post(self.url, data={'type': genre_type, })

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)

        response = self.client.post(self.url, data={'type': '', })

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)


class GenreListViewTest(TestCase):

    def setUp(self):
        self.url = reverse('books:books-genre-list')

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, GenreListView)

    def test_response(self):
        genre1 = Genre.objects.create(type='type1')
        genre2 = Genre.objects.create(type='type2')
        genre3 = Genre.objects.create(type='type3')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, genre1.type)
        self.assertContains(response, genre2.type)
        self.assertContains(response, genre3.type)
