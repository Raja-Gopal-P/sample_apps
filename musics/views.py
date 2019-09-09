from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from .models import Genre, Album, Band


def dummy_response(request, slug):
    return HttpResponse()


class GenreListView(ListView):
    model = Genre
    context_object_name = 'genres'
    template_name = 'musics/genres-list-view.html'


class GenreDetailView(DetailView):
    model = Genre
    slug_url_kwarg = 'slug'
    context_object_name = 'genre'
    template_name = 'musics/genre-detail-view.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['albums'] = kwargs['genre'].albums.all()
        return kwargs


class AlbumListView(ListView):
    model = Album
    context_object_name = 'albums'
    template_name = 'musics/album-list-view.html'


class AlbumDetailView(DetailView):
    model = Album
    slug_url_kwarg = 'slug'
    context_object_name = 'album'
    template_name = 'musics/album-detail-view.html'


class BandListView(ListView):
    model = Band
    context_object_name = 'bands'
    template_name = 'musics/bands-list-view.html'


class BandDetailView(DetailView):
    model = Band
    pk_url_kwarg = 'id'
    context_object_name = 'band'
    template_name = 'musics/band-detail-view.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['albums'] = kwargs['band'].albums.all()
        return kwargs
