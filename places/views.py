from django.views.generic import ListView

from .models import Place


class PlacesListView(ListView):
    context_object_name = 'places'
    model = Place
    template_name = 'places/places-list.html'
