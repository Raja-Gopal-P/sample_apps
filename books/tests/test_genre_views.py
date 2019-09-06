from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Genre
from ..genre_views import GenreCreateView


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

        self.assertRedirects(response, reverse('books:books-list'))
        self.assertTrue(Genre.objects.filter(type=genre_type))

    def test_failure_response(self):
        genre_type = self.genre.type
        response = self.client.post(self.url, data={'type': genre_type, })

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)

        response = self.client.post(self.url, data={'type': '', })

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)
