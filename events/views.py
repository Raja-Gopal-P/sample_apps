from django.shortcuts import render, redirect
from django.views.generic import RedirectView, DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Event
from .filters import EventsDateFilter, EventsMonthFilter, EventsYearFilter
from .forms import EventCreationForm, EventTimingCreationForm


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

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        request = self.request
        event = kwargs['event']
        kwargs['event_admin'] = True

        if event.created_by is not None:
            if request.user is None or request.user.username != event.created_by.username:
                kwargs['event_admin'] = False

        return kwargs


def create_event_view(request):
    user = request.user
    if request.method == 'POST':
        form = EventCreationForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            if isinstance(user, User):
                event.created_by = user
            event.save()
            form.save_m2m()
            return redirect('events:event-view', id=event.id)
    else:
        form = EventCreationForm()
    return render(request, 'events/create_event_view.html', {'form': form})


def add_event_timing_view(request, event_id):
    event = get_object_or_404(Event,pk=event_id)
    if event.created_by is not None:
        if request.user is None or request.user.username != event.created_by.username:
            return redirect('events:event-view', id=event.id)

    if request.method == 'POST':
        form = EventTimingCreationForm(request.POST)
        if form.is_valid():
            event_timing = form.save(commit=False)
            event_timing.event = event
            event_timing.save()
            return redirect('events:event-view', id=event.id)
    else:
        form = EventTimingCreationForm()
    return render(request, 'events/add_event_timing.html', {'event': event,'form': form})
