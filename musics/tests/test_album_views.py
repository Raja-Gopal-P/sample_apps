from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from datetime import date

from ..views import AlbumListView, AlbumDetailView
from ..models import Album, Music


class AlbumListViewTest(TestCase):

    def setUp(self):
        self.url = reverse('musics:music-album-list')

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, AlbumListView)

    def test_success_response(self):
        album = Album.objects.create(title='title', prefix='prefix', subtitle='sub_title', slug='slug1', asin='asin1',
                                     release_date=date(year=2018, month=4, day=20), cover='musics/c1.jpeg', )
        response = self.client.get(self.url)

        self.assertTrue(response.context.get('albums'))
        self.assertContains(response, album.slug)


class AlbumDetailViewTest(TestCase):

    def setUp(self):
        self.album = Album.objects.create(title='title', prefix='prefix', subtitle='sub_title', slug='slug1',
                                          asin='asin1', release_date=date(year=2018, month=4, day=20),
                                          cover='musics/c1.jpeg', )
        self.url = reverse('musics:music-album-detail', kwargs={'slug': self.album.slug, })

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, AlbumDetailView)

    def test_success_response(self):
        music = Music.objects.create(title='title', slug='slug1', album=self.album)
        response = self.client.get(self.url)

        self.assertTrue(response.context.get('album'))
        self.assertContains(response, music.slug)

    def test_404(self):
        url = reverse('musics:music-album-detail', kwargs={'slug': self.album.slug + '_unique', })
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
