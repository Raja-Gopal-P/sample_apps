from django.test import TestCase
from django.db import models
from django.db.utils import IntegrityError

from datetime import date

from ..models import Genre, Label, BandMember, Band, Album, Music


class GenreModelTest(TestCase):

    def test_fields(self):
        self.assertEqual(Genre._meta.get_field('title').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Genre._meta.get_field('slug').get_internal_type(), models.SlugField.__name__)

    def test_unique_title_field(self):
        with self.assertRaises(IntegrityError):
            Genre.objects.create(title='title', slug='slug1')
            Genre.objects.create(title='title', slug='slug2')

    def test_unique_slug_field(self):
        with self.assertRaises(IntegrityError):
            Genre.objects.create(title='title1', slug='slug')
            Genre.objects.create(title='title2', slug='slug')


class LabelModelTest(TestCase):

    def test_fields(self):
        self.assertEqual(Label._meta.get_field('name').get_internal_type(), models.CharField.__name__)

    def test_unique_name_field(self):
        with self.assertRaises(IntegrityError):
            Label.objects.create(name='title')
            Label.objects.create(name='title')


class BandMembersModelTest(TestCase):

    def test_fields(self):
        self.assertEqual(BandMember._meta.get_field('name').get_internal_type(), models.CharField.__name__)
        self.assertEqual(BandMember._meta.get_field('instrument').get_internal_type(), models.CharField.__name__)
        self.assertEqual(BandMember._meta.get_field('address').get_internal_type(), models.CharField.__name__)
        self.assertEqual(BandMember._meta.get_field('phone_number').get_internal_type(), models.CharField.__name__)

    def test_unique_name_field(self):
        with self.assertRaises(IntegrityError):
            BandMember.objects.create(name='name', instrument='Guitar', address='address1',
                                      phone_number='+91-1234567890')
            BandMember.objects.create(name='name', instrument='Guitar', address='address1',
                                      phone_number='+91-1234567891')

    def test_unique_phone_number_field(self):
        with self.assertRaises(IntegrityError):
            BandMember.objects.create(name='name1', instrument='Guitar', address='address1',
                                      phone_number='+91-1234567890')
            BandMember.objects.create(name='name2', instrument='Guitar', address='address1',
                                      phone_number='+91-1234567890')


class BandModelTest(TestCase):

    def test_fields(self):
        self.assertEqual(Band._meta.get_field('name').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Band._meta.get_field('members').get_internal_type(), models.ManyToManyField.__name__)

    def test_unique_name_field(self):
        with self.assertRaises(IntegrityError):
            Band.objects.create(name='name')
            Band.objects.create(name='name')


class AlbumModelTest(TestCase):

    def setUp(self):
        self.band = Band.objects.create(name='name')
        self.label = Label.objects.create(name='title')

    def test_fields(self):
        self.assertEqual(Album._meta.get_field('title').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Album._meta.get_field('prefix').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Album._meta.get_field('subtitle').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Album._meta.get_field('slug').get_internal_type(), models.SlugField.__name__)
        self.assertEqual(Album._meta.get_field('asin').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Album._meta.get_field('release_date').get_internal_type(), models.DateField.__name__)
        self.assertEqual(Album._meta.get_field('cover').get_internal_type(), models.FileField.__name__)
        self.assertEqual(Album._meta.get_field('genre').get_internal_type(), models.ManyToManyField.__name__)
        self.assertEqual(Album._meta.get_field('band').get_internal_type(), models.ForeignKey.__name__)
        self.assertEqual(Album._meta.get_field('label').get_internal_type(), models.ForeignKey.__name__)

    def test_unique_title_field(self):
        with self.assertRaises(IntegrityError):
            Album.objects.create(title='title', prefix='prefix', subtitle='sub_title', slug='slug1', asin='asin1',
                                 release_date=date(year=2018, month=4, day=20), cover='musics/c1.jpeg',
                                 band=self.band, label=self.label)
            Album.objects.create(title='title', prefix='prefix', subtitle='sub_title', slug='slug2', asin='asin2',
                                 release_date=date(year=2018, month=4, day=20), cover='musics/c2.jpeg',
                                 band=self.band, label=self.label)

    def test_unique_slug_field(self):
        with self.assertRaises(IntegrityError):
            Album.objects.create(title='title1', prefix='prefix', subtitle='sub_title', slug='slug', asin='asin1',
                                 release_date=date(year=2018, month=4, day=20), cover='musics/c1.jpeg',
                                 band=self.band, label=self.label)
            Album.objects.create(title='title2', prefix='prefix', subtitle='sub_title', slug='slug', asin='asin2',
                                 release_date=date(year=2018, month=4, day=20), cover='musics/c2.jpeg',
                                 band=self.band, label=self.label)

    def test_unique_asin_field(self):
        with self.assertRaises(IntegrityError):
            Album.objects.create(title='title1', prefix='prefix', subtitle='sub_title', slug='slug1', asin='asin',
                                 release_date=date(year=2018, month=4, day=20), cover='musics/c1.jpeg',
                                 band=self.band, label=self.label)
            Album.objects.create(title='title2', prefix='prefix', subtitle='sub_title', slug='slug2', asin='asin',
                                 release_date=date(year=2018, month=4, day=20), cover='musics/c2.jpeg',
                                 band=self.band, label=self.label)

    def test_unique_cover_field(self):
        with self.assertRaises(IntegrityError):
            Album.objects.create(title='title1', prefix='prefix', subtitle='sub_title', slug='slug1', asin='asin1',
                                 release_date=date(year=2018, month=4, day=20), cover='musics/c.jpeg',
                                 band=self.band, label=self.label)
            Album.objects.create(title='title2', prefix='prefix', subtitle='sub_title', slug='slug2', asin='asin2',
                                 release_date=date(year=2018, month=4, day=20), cover='musics/c.jpeg',
                                 band=self.band, label=self.label)


class MusicModelTest(TestCase):

    def test_fields(self):
        self.assertEqual(Music._meta.get_field('title').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Music._meta.get_field('slug').get_internal_type(), models.SlugField.__name__)
        self.assertEqual(Music._meta.get_field('album').get_internal_type(), models.ForeignKey.__name__)
        self.assertEqual(Music._meta.get_field('band').get_internal_type(), models.ForeignKey.__name__)

    def test_unique_music_title_field(self):
        with self.assertRaises(IntegrityError):
            Music.objects.create(title='title', slug='slug1')
            Music.objects.create(title='title', slug='slug2')

    def test_unique_music_slug_field(self):
        with self.assertRaises(IntegrityError):
            Music.objects.create(title='title1', slug='slug')
            Music.objects.create(title='title2', slug='slug')
