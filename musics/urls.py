from django.urls import path

from .views import GenreListView, GenreDetailView, AlbumListView, AlbumDetailView, dummy_response


app_name = 'musics'

urlpatterns = [
    path('genre/', GenreListView.as_view(), name='music-genre-list'),
    path('genre/<slug:slug>', GenreDetailView.as_view(), name='music-genre-detail'),
    path('', AlbumListView.as_view(), name='music-album-list'),
    path('<slug:slug>/', AlbumDetailView.as_view(), name='music-album-detail'),
    path('music/<slug:slug>/', dummy_response, name='music-music-detail'),
]
