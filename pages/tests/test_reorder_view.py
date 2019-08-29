from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User

from ..models import Page


class PageUpdateViewTest(TestCase):

    def setUp(self):
        self.username = 'test-admin'
        self.email = 'rajagopal@testpress.in'
        self.password = 'password'
        User.objects.create_superuser(username=self.username, email=self.email,
                                      password=self.password)
        Page.objects.create(title='t1', slug='t1', content_html='', )
        Page.objects.create(title='t2', slug='t2', content_html='', )
        Page.objects.create(title='t3', slug='t3', content_html='', )

        self.url = reverse('custom-admin:reorder-pages')

    def test_login_redirect(self):
        redirect_url = '{login_url}?next={next_url}'.format(login_url=reverse('custom-admin:login'), next_url=self.url)
        response = self.client.get(self.url)
        self.assertRedirects(response, redirect_url)

    def test_context_object(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.url)
        self.assertTrue(response.context.get('pages'))

    def test_valid_data(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(self.url, data={
            'items_order': 'item[]=2&item[]=1&item[]=3',
        })
        self.assertEqual(Page.objects.get(title='t2').ordering, 0)
        self.assertEqual(Page.objects.get(title='t1').ordering, 1)
        self.assertRedirects(response, reverse('pages:pages-list'))

        response = self.client.post(self.url, data={
            'items_order': 'item[]=2&item[]=1',
        })
        self.assertEqual(Page.objects.get(title='t2').ordering, 0)
        self.assertEqual(Page.objects.get(title='t1').ordering, 1)
        self.assertEqual(Page.objects.get(title='t3').ordering, 2)
        self.assertRedirects(response, reverse('pages:pages-list'))

        Page.objects.all().delete()
        response = self.client.post(self.url, data={
            'items_order': '',
        })
        self.assertRedirects(response, reverse('pages:pages-list'))

    def test_invalid_data(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.post(self.url, data={
            'items_order': 'item[]=1&item[]=3',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('op_fail'))

        response = self.client.post(self.url, data={
            'items_order': 'item[]=2&item[]=1&item[]=1',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('op_fail'))
