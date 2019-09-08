from django.views.generic import ListView, DetailView

from .models import Genre


class GenreListView(ListView):
    model = Genre
    context_object_name = 'genres'
    template_name = 'movies/genre-list.html'


class GenreDetailView(DetailView):
    model = Genre
    slug_url_kwarg = 'slug'
    context_object_name = 'genre'
    template_name = 'movies/genre-detail-view.html'
