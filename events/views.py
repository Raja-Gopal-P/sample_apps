from django.views.generic import ListView

from .models import Event


class EventListView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'events/events_list_view.html'
