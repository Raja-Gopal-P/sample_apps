from django.shortcuts import render
from django.views.generic import RedirectView, DetailView

from .models import Event
from .filters import EventsDateFilter, EventsMonthFilter, EventsYearFilter


class EventDateFilterRedirect(RedirectView):
    pattern_name = 'events:events-list-date-filter'


def filter_by_date(request):
    events = Event.objects.all()
    events_filter = EventsDateFilter(request.GET, queryset=events)

    return render(request, 'events/events_list_view.html', {'events': events_filter.qs,
                                                            'form': events_filter.form,
                                                            'date_filter': True
                                                            })


def filter_by_month(request):
    events = Event.objects.all()
    events_filter = EventsMonthFilter(request.GET, queryset=events)

    return render(request, 'events/events_list_view.html', {'events': events_filter.qs,
                                                            'form': events_filter.form,
                                                            'month_filter': True
                                                            })


def filter_by_year(request):
    events = Event.objects.all()
    events_filter = EventsYearFilter(request.GET, queryset=events)

    return render(request, 'events/events_list_view.html', {'events': events_filter.qs,
                                                            'form': events_filter.form,
                                                            'year_filter': True
                                                            })


class EventDetailView(DetailView):
    context_object_name = 'event'
    model = Event
    pk_url_kwarg = 'id'
    template_name = 'events/event_view.html'
