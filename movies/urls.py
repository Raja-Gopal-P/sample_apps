from django.urls import path

from .genre_views import GenreListView, GenreDetailView


app_name = 'movies'

urlpatterns = [
    path('genre/', GenreListView.as_view(), name='genre-list'),
    path('genre/<slug:slug>', GenreDetailView.as_view(), name='genre-detail-view'),
]
