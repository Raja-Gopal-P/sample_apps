from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from ..models import BookMark
from ..views import BookmarkDeleteView


class BookmarkDeleteViewTest(TestCase):

    def setUp(self):
        self.bookmark1 = BookMark.objects.create(name='bm1', url='url1')
        self.bookmark2 = BookMark.objects.create(name='bm2', url='url2')

        self.url = reverse('bookmarks:bookmark-delete-view', kwargs={'id': self.bookmark1.id})

    def test_url_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, BookmarkDeleteView)

    def test_delete_api(self):
        response = self.client.post(self.url)
        self.assertRedirects(response, reverse('bookmarks:bookmarks-index-view'))

    def test_404(self):
        url = reverse('bookmarks:bookmark-delete-view', kwargs={'id': self.bookmark2.id + 1})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 404)
