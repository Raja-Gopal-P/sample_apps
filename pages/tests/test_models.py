from django.test import TestCase
from django.db import models
from django.db.utils import IntegrityError
from django_extensions.db.models import TimeStampedModel

from ..models import Page


class PageModelValidation(TestCase):

    def test_field_types(self):
        self.assertEqual(Page._meta.get_field('title').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Page._meta.get_field('slug').get_internal_type(), models.SlugField.__name__)
        self.assertEqual(Page._meta.get_field('content_html').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Page._meta.get_field('ordering').get_internal_type(), models.PositiveSmallIntegerField.__name__)

    def test_default_ordering(self):
        Page.objects.create(title='t1', slug='t1', content_html='', ordering=1)
        Page.objects.create(title='t2', slug='t2', content_html='', ordering=0)
        results = Page.objects.all()
        self.assertEqual("t2", results[0].title)
        self.assertEqual("t1", results[1].title)

    def test_title_field_uniqueness(self):
        with self.assertRaises(IntegrityError):
            Page.objects.create(title='t1', slug='t1', content_html='',)
            Page.objects.create(title='t1', slug='t2', content_html='',)

    def test_slug_field_uniqueness(self):
        with self.assertRaises(IntegrityError):
            Page.objects.create(title='t1', slug='t1', content_html='',)
            Page.objects.create(title='t2', slug='t1', content_html='',)
