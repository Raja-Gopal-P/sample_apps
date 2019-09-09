from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from datetime import date

from ..director_views import DirectorListView, DirectorDetailView
from ..models import Director


class DirectorListViewTest(TestCase):

    def setUp(self):
        self.url = reverse('movies:director-list')

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, DirectorListView)

    def test_view_context(self):
        Director.objects.create(first_name='Fn1', middle_name='mn1', last_name='lm1', phone_number='+91-123456789',
                                birth_date=date(year=2019, month=8, day=23), website='http://www.google.co.in',
                                gender=2)
        response = self.client.get(self.url)

        self.assertTrue(response.context.get('directors'))


class DirectorDetailViewTest(TestCase):

    def setUp(self):
        self.director = Director.objects.create(first_name='Fn1', middle_name='mn1', last_name='lm1',
                                                phone_number='+91-123456789', birth_date=date(year=2019, month=8, day=23),
                                                website='http://www.google.co.in', gender=2)
        self.url = reverse('movies:director-detail-view', kwargs={'id': self.director.id, })

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, DirectorDetailView)

    def test_view_context(self):
        response = self.client.get(self.url)
        self.assertTrue(response.context.get('director'))

    def test_404(self):
        url = reverse('movies:director-detail-view', kwargs={'id': self.director.id + 1, })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
