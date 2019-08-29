from django.contrib.gis.geos import Point
from django.test import TestCase
from django.db import models
from django.contrib.gis.db.models import PointField
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from ..models import Place, City


class CityModelValidation(TestCase):

    def test_field_types(self):
        self.assertEqual(City._meta.get_field('city_name').get_internal_type(), models.CharField.__name__)

    def test_unique_field(self):
        with self.assertRaises(IntegrityError):
            City.objects.create(city_name='Tirunelveli')
            City.objects.create(city_name='Tirunelveli')


class PlacesModelValidation(TestCase):

    def setUp(self):
        self.city1 = City.objects.create(city_name='Tirunelveli')
        self.city2 = City.objects.create(city_name='Trichy')
        self.city3 = City.objects.create(city_name='Madurai')

    def test_field_types(self):
        self.assertEqual(Place._meta.get_field('title').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Place._meta.get_field('location').get_internal_type(), PointField.__name__)
        self.assertEqual(Place._meta.get_field('description').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Place._meta.get_field('address').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Place._meta.get_field('phone').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Place._meta.get_field('types').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Place._meta.get_field('tags').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Place._meta.get_field('city').get_internal_type(), models.ForeignKey.__name__)

    def test_unique_title_field(self):
        with self.assertRaises(IntegrityError):
            Place.objects.create(title='P1', location=Point(5,10), description='Des1', address='add1',
                                 phone='+91-9566563867', types='abc-def', city=self.city1)
            Place.objects.create(title='P1', location=Point(5, 10), description='Des2', address='add2',
                                 phone='+91-9566563868', types='abc-def', city=self.city2)

    def test_unique_phone_field(self):
        with self.assertRaises(IntegrityError):
            Place.objects.create(title='P1', location=Point(5,10), description='Des1', address='add1',
                                 phone='+91-9566563867', types='abc-def', city=self.city1)
            Place.objects.create(title='P2', location=Point(5, 10), description='Des2', address='add2',
                                 phone='+91-9566563867', types='abc-def', city=self.city2)
