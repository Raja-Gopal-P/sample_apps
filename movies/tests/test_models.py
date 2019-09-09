from django.test import TestCase
from django.db import models

from ..models import Studio, Genre, Director, Movie


class StudioModelTest(TestCase):

    def test_fields(self):
        self.assertEqual(Studio._meta.get_field('title').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Studio._meta.get_field('prefix').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Studio._meta.get_field('slug').get_internal_type(), models.SlugField.__name__)
        self.assertEqual(Studio._meta.get_field('website').get_internal_type(), models.CharField.__name__)


class GenreModelTest(TestCase):

    def test_fields(self):
        self.assertEqual(Genre._meta.get_field('title').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Genre._meta.get_field('slug').get_internal_type(), models.SlugField.__name__)


class DirectorModelTest(TestCase):

    def test_fields(self):
        self.assertEqual(Director._meta.get_field('first_name').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Director._meta.get_field('middle_name').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Director._meta.get_field('last_name').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Director._meta.get_field('phone_number').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Director._meta.get_field('birth_date').get_internal_type(), models.DateField.__name__)
        self.assertEqual(Director._meta.get_field('website').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Director._meta.get_field('gender').get_internal_type(),
                         models.PositiveSmallIntegerField.__name__)


class MovieModelTest(TestCase):

    def test_fields(self):
        self.assertEqual(Movie._meta.get_field('title').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Movie._meta.get_field('prefix').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Movie._meta.get_field('sub_title').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Movie._meta.get_field('slug').get_internal_type(), models.SlugField.__name__)
        self.assertEqual(Movie._meta.get_field('released_date').get_internal_type(), models.DateField.__name__)
        self.assertEqual(Movie._meta.get_field('cover_image').get_internal_type(), models.FileField.__name__)
        self.assertEqual(Movie._meta.get_field('review').get_internal_type(),models.FloatField.__name__)
        self.assertEqual(Movie._meta.get_field('asin').get_internal_type(),models.CharField.__name__)
        self.assertEqual(Movie._meta.get_field('studio').get_internal_type(),models.ForeignKey.__name__)
        self.assertEqual(Movie._meta.get_field('directors').get_internal_type(),models.ManyToManyField.__name__)
        self.assertEqual(Movie._meta.get_field('genres').get_internal_type(),models.ManyToManyField.__name__)
