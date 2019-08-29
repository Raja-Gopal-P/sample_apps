from django.views.generic import ListView, DetailView

from .models import Place


class PlacesListView(ListView):
    context_object_name = 'places'
    model = Place
    template_name = 'places/places-list.html'


class PlaceDetailView(DetailView):
    context_object_name = 'place'
    model = Place
    pk_url_kwarg = 'id'
    template_name = 'places/place-view.html'
