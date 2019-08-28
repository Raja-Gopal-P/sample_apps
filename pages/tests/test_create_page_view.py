from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User

from ..models import Page


class PageCreationViewTest(TestCase):

    def setUp(self):
        self.username = 'test-admin'
        self.email = 'rajagopal@testpress.in'
        self.password = 'password'
        User.objects.create_superuser(username=self.username, email=self.email,
                                      password=self.password)

        self.url = reverse('custom-admin:create-page')

    def test_login_redirect(self):
        redirect_url = '{login_url}?next={next_url}'.format(login_url=reverse('custom-admin:login'), next_url=self.url)
        response = self.client.get(self.url)
        self.assertRedirects(response, redirect_url)

    def test_create_new_page_api(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(self.url, data={
            'title': 't3',
            'slug': 't3',
            'content_html': 'Hi',
            'ordering': 0,
        })
        self.assertTrue(Page.objects.exists())
        self.assertRedirects(response, reverse('pages:pages-list'))

        response = self.client.post(self.url, data={
            'title': 't3',
            'slug': 't3',
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
