from django.urls import path

from .genre_views import GenreListView, GenreDetailView
from .studio_views import StudioListView, StudioDetailView
from .director_views import DirectorListView, DirectorDetailView


app_name = 'movies'

urlpatterns = [
    path('genre/', GenreListView.as_view(), name='genre-list'),
    path('genre/<slug:slug>', GenreDetailView.as_view(), name='genre-detail-view'),
    path('studio/', StudioListView.as_view(), name='studio-list'),
    path('studio/<slug:slug>', StudioDetailView.as_view(), name='studio-detail-view'),
    path('director/', DirectorListView.as_view(), name='director-list'),
    path('director/<int:id>', DirectorDetailView.as_view(), name='director-detail-view'),
]
