from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from datetime import date

from ..views import MusicListView, MusicDetailView
from ..models import Music, Album


class AlbumListViewTest(TestCase):

    def setUp(self):
        self.url = reverse('musics:music-music-list')

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, MusicListView)

    def test_success_response(self):
        music = Music.objects.create(title='name', slug='title', )
        response = self.client.get(self.url)

        self.assertTrue(response.context.get('musics'))
        self.assertContains(response, reverse('musics:music-music-detail', kwargs={'slug': music.slug, }))


class AlbumDetailViewTest(TestCase):

    def setUp(self):
        self.music = Music.objects.create(title='name', slug='title', )

        self.url = reverse('musics:music-music-detail', kwargs={'slug': self.music.slug, })

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, MusicDetailView)

    def test_success_response(self):
        response = self.client.get(self.url)

        self.assertTrue(response.context.get('music'))

    def test_404(self):
        url = reverse('musics:music-music-detail', kwargs={'slug': self.music.slug + '_unique', })
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
