from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from datetime import date

from ..movie_views import MovieListView, MovieDetailView
from ..models import Movie, Director, Studio, Genre


class DirectorListViewTest(TestCase):

    def setUp(self):
        self.url = reverse('movies:movie-list')

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, MovieListView)

    def test_view_context(self):
        genre = Genre.objects.create(title='genre1', slug='genre1')
        studio = Studio.objects.create(title='Studio', prefix='prefix',
                                       slug='studio', website='http://www.google.com')
        director = Director.objects.create(first_name='Fn1', middle_name='mn1', last_name='lm1',
                                           phone_number='+91-123456789', birth_date=date(year=2019, month=8, day=23),
                                           website='http://www.google.co.in', gender=2)
        movie = Movie.objects.create(title='Title', prefix='prefix', sub_title='sub_title2', slug='title',
                                     released_date=date(year=2019, month=8, day=3), review=4.6, asin='546789542',
                                     studio=studio, cover_image='movies/m2.jpeg')
        movie.genres.add(genre)
        movie.directors.add(director)
        response = self.client.get(self.url)

        self.assertTrue(response.context.get('movies'))


class DirectorDetailViewTest(TestCase):

    def setUp(self):
        genre = Genre.objects.create(title='genre1', slug='genre1')
        studio = Studio.objects.create(title='Studio', prefix='prefix',
                                       slug='studio', website='http://www.google.com')
        director = Director.objects.create(first_name='Fn1', middle_name='mn1', last_name='lm1',
                                           phone_number='+91-123456789', birth_date=date(year=2019, month=8, day=23),
                                           website='http://www.google.co.in', gender=2)
        self.movie = Movie.objects.create(title='Title', prefix='prefix', sub_title='sub_title2', slug='title',
                                          released_date=date(year=2019, month=8, day=3), review=4.6, asin='546789542',
                                          studio=studio, cover_image='movies/m2.jpeg')
        self.movie.genres.add(genre)
        self.movie.directors.add(director)
        self.url = reverse('movies:movie-detail-view', kwargs={'slug': self.movie.slug, })

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, MovieDetailView)

    def test_view_context(self):
        response = self.client.get(self.url)
        self.assertTrue(response.context.get('movie'))

    def test_404(self):
        url = reverse('movies:movie-detail-view', kwargs={'slug': self.movie.slug + '_unique', })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
