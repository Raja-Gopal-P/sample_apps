from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from ..models import Page
from ..views import PageView


class PageViewTest(TestCase):

    def setUp(self):
        self.page1 = Page.objects.create(title='t1', slug='t1', content_html='<p>Hi</p>', )
        self.url = reverse('pages:page-view', kwargs={'slug': self.page1.slug})
        self.response = self.client.get(self.url)

    def test_view_class(self):
        view = resolve(self.url)
        self.assertEquals(view.func.view_class, PageView)

    def test_context_object_name(self):
        page = self.response.context.get('page')
        self.assertTrue(page)

    def test_rendering(self):
        self.assertContains(self.response, self.page1.content_html)

    def test_page_not_found(self):
        url = reverse('pages:page-view', kwargs={'slug': 't2'})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
