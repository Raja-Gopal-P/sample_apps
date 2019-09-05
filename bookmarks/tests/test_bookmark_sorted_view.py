from django.shortcuts import reverse
from django.urls import resolve

from .test_bookmark_filters import BookmarkListViewTest
from ..views import bookmarks_sorted_filter
from ..models import BookMark


class BookmarkSortedListView(BookmarkListViewTest):

    def setUp(self):
        super().setUp()
        self.url = reverse('bookmarks:bookmarks-sorted-view')

    def test_url_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func, bookmarks_sorted_filter)

    def test_sort_by_name(self):
        bookmark = BookMark.objects.create(name='A', url='http://www.test.co/', description='description')
        response = self.client.get(self.url)
        bookmarks = response.context.get('bookmarks')

        self.assertEqual(bookmarks[0], bookmark)
