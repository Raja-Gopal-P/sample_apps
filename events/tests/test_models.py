from django.test import TestCase
from django.db import models
from django.contrib.gis.geos import Point
from django.db.utils import IntegrityError
from django.utils.timezone import localtime, localdate

from datetime import datetime, timedelta

from places.models import City, Place

from ..models import Event, EventTiming


class EventTestMeta(TestCase):

    def setUp(self):
        self.city = City.objects.create(city_name='City1')
        self.place = Place.objects.create(title='Place1', location=Point(1,2), description='Desc', address='addr',
                                          phone='+91-1234567890', city=self.city, types='Type1', tags='Tag1')
        self.event = Event.objects.create(title='Event', date=localdate(), place=self.place, )


class EventModelTest(EventTestMeta):

    def test_field_types(self):
        self.assertEqual(Event._meta.get_field('title').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Event._meta.get_field('full_day_event').get_internal_type(), models.BooleanField.__name__)
        self.assertEqual(Event._meta.get_field('place').get_internal_type(), models.ForeignKey.__name__)
        self.assertEqual(Event._meta.get_field('created_by').get_internal_type(), models.ForeignKey.__name__)
        self.assertEqual(Event._meta.get_field('created').get_internal_type(), models.DateTimeField.__name__)
        self.assertEqual(Event._meta.get_field('modified').get_internal_type(), models.DateTimeField.__name__)

    def test_unique_title(self):
        with self.assertRaises(IntegrityError):
            Event.objects.create(title='Event', date=self.event.date, place=self.place,)

    def test_same_event_another_day(self):
        Event.objects.create(title='Event', date=datetime(year=2019, month=8, day=26).date(), place=self.place,)


class EventTimingModelTest(EventTestMeta):

    def setUp(self):
        super().setUp()
        self.time = localtime()
        self.time_delta = timedelta(minutes=30)
        self.timing1 = EventTiming.objects.create(event=self.event, start_time=self.time,
                                                  end_time=self.time + self.time_delta)

    def test_field_types(self):
        self.assertEqual(EventTiming._meta.get_field('event').get_internal_type(), models.ForeignKey.__name__)
        self.assertEqual(EventTiming._meta.get_field('start_time').get_internal_type(), models.TimeField.__name__)
        self.assertEqual(EventTiming._meta.get_field('end_time').get_internal_type(), models.TimeField.__name__)

    def test_unique_time_interval(self):
        with self.assertRaises(IntegrityError):
            EventTiming.objects.create(event=self.event, start_time=self.timing1.start_time,
                                       end_time=self.timing1.end_time)

    def test_overlapping_interval(self):
        EventTiming.objects.create(event=self.event, start_time=self.timing1.start_time + self.time_delta,
                                   end_time=self.timing1.end_time + self.time_delta)
        EventTiming.objects.create(event=self.event, start_time=self.timing1.start_time - self.time_delta,
                                   end_time=self.timing1.end_time - self.time_delta)

    def test_valid_time_interval(self):
        with self.assertRaises(IntegrityError):
            EventTiming.objects.create(event=self.event, start_time=self.timing1.start_time + self.time_delta,
                                       end_time=self.timing1.end_time)
