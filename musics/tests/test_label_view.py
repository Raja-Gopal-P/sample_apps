from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from datetime import date

from ..views import LabelListView, LabelDetailView
from ..models import Label, Album


class AlbumListViewTest(TestCase):

    def setUp(self):
        self.url = reverse('musics:music-label-list')

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, LabelListView)

    def test_success_response(self):
        label = Label.objects.create(name='name')
        response = self.client.get(self.url)

        self.assertTrue(response.context.get('labels'))
        self.assertContains(response, reverse('musics:music-label-detail', kwargs={'id': label.id, }))


class AlbumDetailViewTest(TestCase):

    def setUp(self):
        self.label = Label.objects.create(name='name')

        self.url = reverse('musics:music-label-detail', kwargs={'id': self.label.id, })

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, LabelDetailView)

    def test_success_response(self):
        album = Album.objects.create(title='title', prefix='prefix', subtitle='sub_title', slug='slug1',
                                     asin='asin1', release_date=date(year=2018, month=4, day=20),
                                     cover='musics/c1.jpeg', label=self.label)
        response = self.client.get(self.url)

        self.assertTrue(response.context.get('label'))
        self.assertTrue(response.context.get('albums'))
        self.assertContains(response, reverse('musics:music-album-detail', kwargs={'slug': album.slug, }))

    def test_404(self):
        url = reverse('musics:music-label-detail', kwargs={'id': self.label.id + 1, })
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
