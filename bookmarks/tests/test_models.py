from django.test import TestCase
from django.db import models
from django.db.utils import IntegrityError

from ..models import BookMark


class EventModelTest(TestCase):

    def test_field_types(self):
        self.assertEqual(BookMark._meta.get_field('name').get_internal_type(), models.CharField.__name__)
        self.assertEqual(BookMark._meta.get_field('url').get_internal_type(), models.CharField.__name__)
        self.assertEqual(BookMark._meta.get_field('description').get_internal_type(), models.TextField.__name__)

    def test_unique_name_field(self):
        with self.assertRaises(IntegrityError):
            BookMark.objects.create(name='BM1', url='url1')
            BookMark.objects.create(name='BM1', url='url1')

    def test_unique_url_field(self):
        with self.assertRaises(IntegrityError):
            BookMark.objects.create(name='BM1', url='url1')
            BookMark.objects.create(name='BM2', url='url1')
