from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from ..models import BookMark
from ..views import BookmarkAddTagView


class PageUpdateViewTest(TestCase):

    def setUp(self):
        self.bookmark1 = BookMark.objects.create(name='bm1', url='url1')

        self.url = reverse('bookmarks:bookmark-add-tag-view', kwargs={'id': self.bookmark1.id})

    def test_view_class(self):
        view = resolve(self.url)
        self.assertEquals(view.func.view_class, BookmarkAddTagView)

    def test_add_tag_api(self):
        response = self.client.post(self.url, data={
            'tags': 't1',
        })
        self.assertEqual(self.bookmark1.tags.first().name, 't1')
        self.assertRedirects(response, reverse('bookmarks:bookmarks-index-view'))

        response = self.client.post(self.url, data={
            'tags': '',
        })
        self.assertEqual(self.bookmark1.tags.first().name, 't1')
        self.assertRedirects(response, reverse('bookmarks:bookmarks-index-view'))

    def test_page_not_found(self):
        response = self.client.get(reverse('bookmarks:bookmark-add-tag-view', kwargs={'id': 0}))
        self.assertEqual(response.status_code, 404)
