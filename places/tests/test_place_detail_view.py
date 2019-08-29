from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve
from django.contrib.gis.geos import Point

from ..models import City, Place
from ..views import PlaceDetailView


class PageViewTest(TestCase):

    def setUp(self):
        city = City.objects.create(city_name='Tirunelveli')
        place = Place.objects.create(title='P1', location=Point(5, 10), description='Des1', address='add1',
                             phone='+91-9566563867', types='abc-def', city=city)
        self.url = reverse('places:place-view', kwargs={'id': place.id})
        self.response = self.client.get(self.url)

    def test_view_class(self):
        view = resolve(self.url)
        self.assertEquals(view.func.view_class, PlaceDetailView)

    def test_context_object_name(self):
        place = self.response.context.get('place')
        self.assertTrue(place)

    def test_page_not_found(self):
        url = reverse('places:place-view', kwargs={'id': 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
