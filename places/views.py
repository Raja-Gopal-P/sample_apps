from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Place
from .forms import CreatePlaceForm


class PlacesListView(ListView):
    context_object_name = 'places'
    model = Place
    template_name = 'places/places-list.html'


class PlaceDetailView(DetailView):
    context_object_name = 'place'
    model = Place
    pk_url_kwarg = 'id'
    template_name = 'places/place-view.html'


class PlaceCreateView(CreateView):
    success_url = reverse_lazy('places:places-list')
    form_class = CreatePlaceForm
    template_name = 'places/create-place.html'
