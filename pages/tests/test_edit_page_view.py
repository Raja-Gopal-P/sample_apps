from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve
from django.contrib.auth.models import User

from ..models import Page
from ..views import PageUpdateView


class PageUpdateViewTest(TestCase):

    def setUp(self):
        self.username = 'test-admin'
        self.email = 'rajagopal@testpress.in'
        self.password = 'password'
        User.objects.create_superuser(username=self.username, email=self.email,
                                      password=self.password)
        Page.objects.create(title='t1', slug='t1', content_html='', )
        Page.objects.create(title='t2', slug='t2', content_html='', )

        self.url = reverse('custom-admin:edit-page', kwargs={'slug': 't1'})

    def test_view_class(self):
        view = resolve(self.url)
        self.assertEquals(view.func.view_class, PageUpdateView)

    def test_login_redirect(self):
        redirect_url = '{login_url}?next={next_url}'.format(login_url=reverse('custom-admin:login'), next_url=self.url)
        response = self.client.get(self.url)
        self.assertRedirects(response, redirect_url)

    def test_edit_page_api(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(self.url, data={
            'title': 't3',
            'slug': 't1',
            'content_html': 'Hi',
            'ordering': 0,
        })
        self.assertEqual(Page.objects.get(slug='t1').title, 't3')
        self.assertRedirects(response, reverse('pages:pages-list'))

        response = self.client.post(self.url, data={
            'title': 't2',
            'slug': 't1',
            'content_html': 'Hi',
            'ordering': 0,
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)

        response = self.client.post(self.url, data={
            'title': '',
            'slug': '',
            'content_html': '',
            'ordering': 0,
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)

    def test_page_not_found(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('custom-admin:edit-page', kwargs={'slug': 't3'}))
        self.assertEqual(response.status_code, 404)
