from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from ..models import BookMark
from ..views import BookmarkCreateView


class EventCreationViewTest(TestCase):

    def setUp(self):
        self.url = reverse('bookmarks:bookmarks-create-view')

    def test_view_class(self):
        view = resolve(self.url)
        self.assertEquals(view.func.view_class, BookmarkCreateView)

    def test_create_valid_bookmark(self):
        response = self.client.post(self.url, data={
            'name': 'name',
            'url': 'http://www.test.co/',
            'description': 'description',
        })

        self.assertTrue(BookMark.objects.exists(), msg='Bookmark not added')
        self.assertRedirects(response, reverse('bookmarks:bookmarks-index-view'))

    def test_create_invalid_bookmark(self):

        response = self.client.post(self.url, data={
            'name': '',
            'url': '',
            'description': '',
        })

        self.assertFalse(BookMark.objects.exists())
        self.assertRedirects(response, reverse('bookmarks:bookmarks-index-view'))

    def test_unique_bookmark_creation(self):

        BookMark.objects.create(name='name', url='http://www.test.co/', description='description')
        count = BookMark.objects.count()

        response = self.client.post(self.url, data={
            'name': 'name',
            'url': 'http://www.test.co/',
            'description': 'description',
        })

        self.assertEqual(BookMark.objects.count(), count)
        self.assertRedirects(response, reverse('bookmarks:bookmarks-index-view'))

        response = self.client.post(self.url, data={
            'name': 'name1',
            'url': 'http://www.test.co/',
            'description': 'description',
        })

        self.assertEqual(BookMark.objects.count(), count)
        self.assertRedirects(response, reverse('bookmarks:bookmarks-index-view'))
