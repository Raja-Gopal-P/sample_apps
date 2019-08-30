from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point

from ..models import Place, City
from ..views import PlaceCreateView


class PlaceCreateViewTest(TestCase):

    def setUp(self):
        self.username = 'test-admin'
        self.email = 'rajagopal@testpress.in'
        self.password = 'password'
        User.objects.create_superuser(username=self.username, email=self.email,
                                      password=self.password)

        self.city = City.objects.create(city_name='City1')

        self.url = reverse('custom-admin:create-place')

    def test_view_class(self):
        view = resolve(self.url)
        self.assertEquals(view.func.view_class, PlaceCreateView)

    def test_login_redirect(self):
        redirect_url = '{login_url}?next={next_url}'.format(login_url=reverse('custom-admin:login'), next_url=self.url)
        response = self.client.get(self.url)
        self.assertRedirects(response, redirect_url)

    def test_create_new_place_api(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(self.url, data={
            'title': 'P1',
            'location': str(Point(5, 10)),
            'description': 'Des1',
            'address': 'add1',
            'phone': '+91-9566563867',
            'types': 'abc-def',
            'city': 1,
            'tags': 'tag'
        })
        self.assertTrue(Place.objects.exists())
        self.assertRedirects(response, reverse('places:places-list'))

        response = self.client.post(self.url, data={
            'title': 'P1',
            'location': Point(5, 10),
            'description': 'Des1',
            'address': 'add1',
            'phone': '+91-9566563867',
            'types': 'abc-def',
            'city': self.city,
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)

        response = self.client.post(self.url, data={
            'title': '',
            'location': '',
            'description': '',
            'address': '',
            'phone': '',
            'types': '',
            'city': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)
