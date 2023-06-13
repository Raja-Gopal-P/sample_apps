from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from ..models import BookMark
from ..views import BookmarkUpdateView


class PageUpdateViewTest(TestCase):

    def setUp(self):
        self.bookmark1 = BookMark.objects.create(name='bm1', url='url1')

        self.url = reverse('bookmarks:bookmark-update-view', kwargs={'id': self.bookmark1.id})

    def test_view_class(self):
        view = resolve(self.url)
        self.assertEquals(view.func.view_class, BookmarkUpdateView)

    def test_update_bookmark_api(self):
        response = self.client.post(self.url, data={
            'name': 'name',
            'url': 'http://www.test.co/',
            'description': 'description',
        })
        self.bookmark1.refresh_from_db()
        self.assertEqual(self.bookmark1.name, 'name')
        self.assertRedirects(response, reverse('bookmarks:bookmarks-index-view'))

        response = self.client.post(self.url, data={
            'name': 'name',
            'url': 'http://www.test.co/',
            'description': 'D',
        })
        self.bookmark1.refresh_from_db()
        self.assertEqual(self.bookmark1.description, 'D')
        self.assertRedirects(response, reverse('bookmarks:bookmarks-index-view'))

        response = self.client.post(self.url, data={
            'name': '',
            'url': '',
            'description': 'D',
        })
        self.bookmark1.refresh_from_db()
        self.assertNotEqual(self.bookmark1.name, '')
        self.assertRedirects(response, reverse('bookmarks:bookmarks-index-view'))

    def test_page_not_found(self):
        response = self.client.get(reverse('bookmarks:bookmark-update-view', kwargs={'id': 0}))
        self.assertEqual(response.status_code, 404)
