from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from ..models import Page
from ..views import PagesListView


class PagesListViewTest(TestCase):

    def setUp(self):
        self.page1 = Page.objects.create(title='t1', slug='t1', content_html='', )
        self.page2 = Page.objects.create(title='t2', slug='t2', content_html='', )
        self.url = reverse('pages:pages-list')
        self.response = self.client.get(self.url)

    def test_view_class(self):
        view = resolve(self.url)
        self.assertEquals(view.func.view_class, PagesListView)

    def test_context_object_name(self):
        pages = self.response.context.get('pages')
        self.assertTrue(pages)

    def test_rendering(self):
        self.assertContains(self.response, '>{}</a>'.format(self.page1.title))
        self.assertContains(self.response, '>{}</a>'.format(self.page2.title))
