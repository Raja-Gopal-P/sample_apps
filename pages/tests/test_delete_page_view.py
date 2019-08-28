from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve
from django.contrib.auth.models import User

from ..models import Page
from ..views import PageDeleteView


class PageDeleteViewTest(TestCase):

    def setUp(self):
        self.username = 'test-admin'
        self.email = 'rajagopal@testpress.in'
        self.password = 'password'
        User.objects.create_superuser(username=self.username, email=self.email,
                                      password=self.password)
        Page.objects.create(title='t1', slug='t1', content_html='', )
        Page.objects.create(title='t2', slug='t2', content_html='', )

        self.url = reverse('custom-admin:delete-page', kwargs={'slug': 't1'})

    def test_view_class(self):
        view = resolve(self.url)
        self.assertEquals(view.func.view_class, PageDeleteView)

    def test_login_redirect(self):
        redirect_url = '{login_url}?next={next_url}'.format(login_url=reverse('custom-admin:login'), next_url=self.url)
        response = self.client.get(self.url)
        self.assertRedirects(response, redirect_url)

    def test_delete_page_api(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(self.url)
        self.assertRedirects(response, reverse('pages:pages-list'))

        response = self.client.post(reverse('custom-admin:delete-page', kwargs={'slug': 't2'}))
        self.assertFalse(Page.objects.exists())

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)
