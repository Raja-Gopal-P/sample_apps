from django.shortcuts import reverse
from django.urls import resolve

from .test_models import EventTestMeta
from ..views import EventDetailView


class EventDetailViewTest(EventTestMeta):

    def setUp(self):
        super().setUp()
        self.url = reverse('events:event-view', kwargs={'id': self.event.id})
        self.response = self.client.get(self.url)

    def test_view_class(self):
        view = resolve(self.url)
        self.assertEquals(view.func.view_class, EventDetailView)

    def test_context_object_name(self):
        place = self.response.context.get('event')
        self.assertTrue(place)

    def test_page_not_found(self):
        url = reverse('places:place-view', kwargs={'id': 0})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
