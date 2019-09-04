from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from ..models import BookMark
from ..views import bookmarks_filter


class BookmarkListViewTest(TestCase):

    def setUp(self):
        self.bookmark1 = BookMark.objects.create(name='bm1', url='url1')
        self.bookmark2 = BookMark.objects.create(name='bm2', url='url2')

        self.url = reverse('bookmarks:bookmarks-index-view')

    def test_url_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func, bookmarks_filter)

    def test_unfiltered_bookmarks_list(self):
        response = self.client.get(self.url)

        self.assertTrue(response.context.get('bookmarks'))
        self.assertTrue(response.context.get('form'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response,self.bookmark1.name)
        self.assertContains(response,self.bookmark2.name)

    def test_filtered_bookmarks(self):
        bookmark = BookMark.objects.create(name='app', url='url3')
        response = self.client.get(self.url, data={'filter_by': bookmark.name[1:2]})

        self.assertTrue(response.context.get('bookmarks'))
        self.assertTrue(response.context.get('form'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, bookmark.name)
        self.assertNotContains(response, self.bookmark1.name)
        self.assertNotContains(response, self.bookmark2.name)

    def test_invalid_query_string_ignore(self):
        response = self.client.get(self.url, data={'filter': self.bookmark1.name[1:2]})

        self.assertTrue(response.context.get('bookmarks'))
        self.assertTrue(response.context.get('form'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.bookmark1.name)
        self.assertContains(response, self.bookmark2.name)
