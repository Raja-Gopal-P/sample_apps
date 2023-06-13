from django.urls import path

from .views import GenreListView, GenreDetailView, AlbumListView, AlbumDetailView, BandListView, BandDetailView, \
    LabelListView, LabelDetailView, MusicListView, MusicDetailView


app_name = 'musics'

urlpatterns = [
    path('genre/', GenreListView.as_view(), name='music-genre-list'),
    path('genre/<slug:slug>', GenreDetailView.as_view(), name='music-genre-detail'),
    path('band/', BandListView.as_view(), name='music-band-list'),
    path('band/<int:id>', BandDetailView.as_view(), name='music-band-detail'),
    path('label/', LabelListView.as_view(), name='music-label-list'),
    path('label/<int:id>', LabelDetailView.as_view(), name='music-label-detail'),
    path('album/', AlbumListView.as_view(), name='music-album-list'),
    path('album/<slug:slug>/', AlbumDetailView.as_view(), name='music-album-detail'),
    path('', MusicListView.as_view(), name='music-music-list'),
    path('<slug:slug>/', MusicDetailView.as_view(), name='music-music-detail'),
]
