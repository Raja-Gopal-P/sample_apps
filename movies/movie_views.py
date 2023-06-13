from django.views.generic import ListView, DetailView

from .models import Movie


class MovieListView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'movies/movie-list.html'


class MovieDetailView(DetailView):
    model = Movie
    slug_url_kwarg = 'slug'
    context_object_name = 'movie'
    template_name = 'movies/movie-detail-view.html'
