from django.shortcuts import reverse
from django.urls import resolve
from django.utils.timezone import localdate

from ..models import Event
from .test_models import EventTestMeta
from ..views import EventListView


class EventsListViewTest(EventTestMeta):

    def setUp(self):
        super().setUp()
        self.event2 = Event.objects.create(title='Event1', date=localdate(), place=self.place, )
        self.url = reverse('events:events-list')
        self.response = self.client.get(self.url)

    def test_view_class(self):
        view = resolve(self.url)
        self.assertEquals(view.func.view_class, EventListView)

    def test_context_object_name(self):
        events = self.response.context.get('events')
        self.assertTrue(events)

    def test_rendering(self):
        self.assertContains(self.response, '>{}</a>'.format(self.event.title))
        self.assertContains(self.response, '>{}</a>'.format(self.event2.title))
