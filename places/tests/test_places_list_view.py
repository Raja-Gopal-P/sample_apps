from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve
from django.contrib.gis.geos import Point

from ..models import Place, City
from ..views import filter_places


class PlacesListViewTest(TestCase):

    def setUp(self):
        self.city1 = City.objects.create(city_name='City1')
        self.city2 = City.objects.create(city_name='City2')
        self.place1 = Place.objects.create(title='P1', location=Point(5, 10), description='Des1', address='add1',
                                           phone='+91-9566563867', types='abc-def', city=self.city1)
        self.place2 = Place.objects.create(title='P2', location=Point(5, 10), description='Des2', address='add2',
                                           phone='+91-9566563868', types='abc-def', city=self.city2)

        self.url = reverse('places:places-list')
        self.response = self.client.get(self.url)

    def test_view_class(self):
        view = resolve(self.url)
        self.assertEquals(view.func, filter_places)

    def test_context_object_name(self):
        places = self.response.context.get('places')
        self.assertTrue(places)

    def test_rendering(self):
        self.assertContains(self.response, '>{}</a>'.format(self.place1.title))
        self.assertContains(self.response, '>{}</a>'.format(self.place2.title))

    def test_places_city_filter(self):
        url = '{}?city={}'.format(self.url, self.city1.id)
        response = self.client.get(url)
        self.assertContains(response, '>{}</a>'.format(self.place1.title))
        self.assertNotContains(response, '>{}</a>'.format(self.place2.title))
