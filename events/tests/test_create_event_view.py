from django.shortcuts import reverse
from django.urls import resolve
from django.contrib.auth.models import User

from datetime import date

from ..models import Event
from .test_models import EventTestMeta
from ..views import create_event_view


class EventCreationViewTest(EventTestMeta):

    def setUp(self):
        super().setUp()
        self.username = 'test-admin'
        self.email = 'rajagopal@testpress.in'
        self.password = 'password'
        User.objects.create_superuser(username=self.username, email=self.email,
                                      password=self.password)

        self.url = reverse('events:create-event')

    def test_view_class(self):
        view = resolve(self.url)
        self.assertEquals(view.func, create_event_view)

    def test_create_anonymous_event(self):
        response = self.client.post(self.url, data={
            'title': 'EventTestAnonymous',
            'date': '2019-09-25',
            'full_day_event': 'on',
            'place': self.place.id,
            'tags': 'tag1 tag2',
        })
        created_event = Event.objects.get(title='EventTestAnonymous')
        self.assertTrue(created_event)
        self.assertRedirects(response, reverse('events:event-view', kwargs={'id': created_event.id}))

    def test_create_new_event_api(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(self.url, data={
            'title': self.event2.title,
            'date': '',
            'place': '',
            'tags': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)

        response = self.client.post(self.url, data={
            'title': self.event2.title,
            'date': self.event2.date.__str__(),
            'full_day_event': 'on',
            'place': self.event2.place.id,
            'tags': 'tag1 tag2',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)

        response = self.client.post(self.url, data={
            'title': self.event2.title,
            'date': date(
                year=self.event2.date.year + 1,
                month=self.event2.date.month,
                day=self.event2.date.day,
            ).__str__(),
            'full_day_event': 'on',
            'place': self.event2.place.id,
            'tags': 'tag1 tag2',
        })
        created_event = Event.objects.get(title=self.event2.title, date=date(
                year=self.event2.date.year + 1,
                month=self.event2.date.month,
                day=self.event2.date.day,
            ))
        self.assertTrue(created_event)
        self.assertRedirects(response, reverse('events:event-view', kwargs={'id': created_event.id}))
        self.client.logout()
