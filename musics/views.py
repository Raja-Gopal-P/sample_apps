from django.views.generic import ListView, DetailView

from .models import Genre, Album, Band, Label, Music


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

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['musics'] = kwargs['album'].musics.all()
        return kwargs


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


class LabelListView(ListView):
    model = Label
    context_object_name = 'labels'
    template_name = 'musics/labels-list-view.html'


class LabelDetailView(DetailView):
    model = Label
    pk_url_kwarg = 'id'
    context_object_name = 'label'
    template_name = 'musics/label-detail-view.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['albums'] = kwargs['label'].albums.all()
        return kwargs


class MusicListView(ListView):
    model = Music
    context_object_name = 'musics'
    template_name = 'musics/musics-list-view.html'


class MusicDetailView(DetailView):
    model = Music
    slug_url_kwarg = 'slug'
    context_object_name = 'music'
    template_name = 'musics/music-detail-view.html'
