from django.shortcuts import reverse
from django.urls import resolve

from datetime import date

from .test_models import EventTestMeta
from ..views import filter_by_date, filter_by_month, filter_by_year
from ..models import Event


class EventsFilterByDateTest(EventTestMeta):

    def setUp(self):
        super().setUp()
        self.url = reverse('events:events-list-date-filter')

    def test_view_class(self):
        view = resolve(self.url)
        self.assertEquals(view.func, filter_by_date)

    def test_context_object_name(self):
        response = self.client.get(self.url)
        events = response.context.get('events')
        self.assertTrue(events)

    def test_rendering(self):
        response = self.client.get(self.url)
        self.assertContains(response, '>{}</a>'.format(self.event.title))
        self.assertContains(response, '>{}</a>'.format(self.event2.title))

    def test_invalid_filter_input(self):
        url = '{url}?date={date}'.format(url=self.url, date='{}-{}-{}'.format(self.event.date.day,
                                                                              self.event.date.month,
                                                                              self.event.date.year))
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)

    def test_valid_date_filter_response(self):
        url = '{url}?date={date}'.format(url=self.url, date=self.event2.date.__str__())
        response = self.client.get(url)
        events = response.context.get('events')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.event2 in events)
        self.assertFalse(self.event in events)


class EventsFilterByMonthTest(EventTestMeta):

    def setUp(self):
        super().setUp()
        self.url = reverse('events:events-list-month-filter')

    def test_view_class(self):
        view = resolve(self.url)
        self.assertEquals(view.func, filter_by_month)

    def test_context_object_name(self):
        response = self.client.get(self.url)
        events = response.context.get('events')
        self.assertTrue(events)

    def test_rendering(self):
        response = self.client.get(self.url)
        self.assertContains(response, '>{}</a>'.format(self.event.title))
        self.assertContains(response, '>{}</a>'.format(self.event2.title))

    def test_invalid_filter_input(self):
        url = '{url}?month={month}'.format(url=self.url, month=0)
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)

    def test_valid_month_filter_response(self):
        url = '{url}?month={month}'.format(url=self.url, month=self.event2.date.month)
        response = self.client.get(url)
        events = response.context.get('events')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.event2 in events)
        self.assertFalse(self.event in events)


class EventsFilterByYearTest(EventTestMeta):

    def setUp(self):
        super().setUp()
        self.url = reverse('events:events-list-year-filter')

    def test_view_class(self):
        view = resolve(self.url)
        self.assertEquals(view.func, filter_by_year)

    def test_context_object_name(self):
        response = self.client.get(self.url)
        events = response.context.get('events')
        self.assertTrue(events)

    def test_rendering(self):
        response = self.client.get(self.url)
        self.assertContains(response, '>{}</a>'.format(self.event.title))
        self.assertContains(response, '>{}</a>'.format(self.event2.title))

    def test_invalid_filter_input(self):
        url = '{url}?year={year}'.format(url=self.url, year=0)
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)

    def test_valid_month_filter_response(self):
        event = Event.objects.create(title='Event', date=date(year=2017, month=8, day=26), place=self.place, )
        url = '{url}?year={year}'.format(url=self.url, year=self.event2.date.year)
        response = self.client.get(url)
        events = response.context.get('events')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.event2 in events)
        self.assertFalse(event in events)
