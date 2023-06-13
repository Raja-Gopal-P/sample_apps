from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from datetime import date

from ..views import GenreListView, GenreDetailView
from ..models import Genre, Album


class GenreListViewTest(TestCase):

    def setUp(self):
        self.url = reverse('musics:music-genre-list')

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, GenreListView)

    def test_success_response(self):
        genre = Genre.objects.create(title='title1', slug='title1')
        response = self.client.get(self.url)

        self.assertTrue(response.context.get('genres'))
        self.assertContains(response, genre.slug)


class GenreDetailViewTest(TestCase):

    def setUp(self):
        self.genre = Genre.objects.create(title='title1', slug='title1')
        self.url = reverse('musics:music-genre-detail', kwargs={'slug': self.genre.slug, })

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, GenreDetailView)

    def test_success_response(self):
        album = Album.objects.create(title='title', prefix='prefix', subtitle='sub_title', slug='slug1',
                                     asin='asin1', release_date=date(year=2018, month=4, day=20),
                                     cover='musics/c1.jpeg', )
        album.genre.add(self.genre)
        response = self.client.get(self.url)

        self.assertTrue(response.context.get('genre'))
        self.assertTrue(response.context.get('albums'))
        self.assertContains(response, album.slug)

    def test_404(self):
        url = reverse('musics:music-genre-detail', kwargs={'slug': self.genre.slug + '_unique', })
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
