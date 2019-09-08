from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from ..genre_views import GenreListView, GenreDetailView
from ..models import Genre


class GenreListViewTest(TestCase):

    def setUp(self):
        self.url = reverse('movies:genre-list')

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, GenreListView)

    def test_view_context(self):
        Genre.objects.create(title='genre1', slug='genre1')
        response = self.client.get(self.url)

        self.assertTrue(response.context.get('genres'))


class GenreDetailViewTest(TestCase):

    def setUp(self):
        self.genre = Genre.objects.create(title='genre1', slug='genre1')
        self.url = reverse('movies:genre-detail-view', kwargs={'slug': self.genre.slug, })

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, GenreDetailView)

    def test_view_context(self):
        response = self.client.get(self.url)
        self.assertTrue(response.context.get('genre'))

    def test_404(self):
        url = reverse('movies:genre-detail-view', kwargs={'slug': self.genre.slug + '_unique', })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
