from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from ..studio_views import StudioListView, StudioDetailView
from ..models import Studio


class GenreListViewTest(TestCase):

    def setUp(self):
        self.url = reverse('movies:studio-list')

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, StudioListView)

    def test_view_context(self):
        Studio.objects.create(title='Studio', prefix='prefix',
                              slug='studio', website='http://www.google.com')
        response = self.client.get(self.url)

        self.assertTrue(response.context.get('studios'))


class GenreDetailViewTest(TestCase):

    def setUp(self):
        self.studio = Studio.objects.create(title='Studio', prefix='prefix',
                                           slug='studio', website='http://www.google.com')
        self.url = reverse('movies:studio-detail-view', kwargs={'slug': self.studio.slug, })

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, StudioDetailView)

    def test_view_context(self):
        response = self.client.get(self.url)
        self.assertTrue(response.context.get('studio'))

    def test_404(self):
        url = reverse('movies:genre-detail-view', kwargs={'slug': self.studio.slug + '_unique', })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
