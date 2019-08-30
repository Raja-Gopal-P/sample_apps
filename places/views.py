from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Place
from .forms import CreatePlaceForm
from .filters import PlacesCityFilter


class PlacesListView(ListView):
    context_object_name = 'places'
    model = Place
    template_name = 'places/places-list.html'


def filter_places(request):
    places = Place.objects.all()
    places_filter = PlacesCityFilter(request.GET, queryset=places)

    return render(request, 'places/places-list.html', {'places': places_filter.qs, 'form': places_filter.form})


class PlaceDetailView(DetailView):
    context_object_name = 'place'
    model = Place
    pk_url_kwarg = 'id'
    template_name = 'places/place-view.html'


class PlaceCreateView(CreateView):
    success_url = reverse_lazy('places:places-list')
    form_class = CreatePlaceForm
    template_name = 'places/create-place.html'
