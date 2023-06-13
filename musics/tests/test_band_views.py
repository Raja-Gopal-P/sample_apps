from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from datetime import date

from ..views import BandListView, BandDetailView
from ..models import Band, Album


class AlbumListViewTest(TestCase):

    def setUp(self):
        self.url = reverse('musics:music-band-list')

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, BandListView)

    def test_success_response(self):
        band = Band.objects.create(name='name')
        response = self.client.get(self.url)

        self.assertTrue(response.context.get('bands'))
        self.assertContains(response, reverse('musics:music-band-detail', kwargs={'id': band.id, }))


class AlbumDetailViewTest(TestCase):

    def setUp(self):
        self.band = Band.objects.create(name='name')

        self.url = reverse('musics:music-band-detail', kwargs={'id': self.band.id, })

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, BandDetailView)

    def test_success_response(self):
        album = Album.objects.create(title='title', prefix='prefix', subtitle='sub_title', slug='slug1',
                                     asin='asin1', release_date=date(year=2018, month=4, day=20),
                                     cover='musics/c1.jpeg', band=self.band)
        response = self.client.get(self.url)

        self.assertTrue(response.context.get('band'))
        self.assertTrue(response.context.get('albums'))
        self.assertContains(response, reverse('musics:music-album-detail', kwargs={'slug': album.slug, }))

    def test_404(self):
        url = reverse('musics:music-band-detail', kwargs={'id': self.band.id + 1, })
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
