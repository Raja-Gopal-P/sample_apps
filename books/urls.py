from django.urls import path

from .book_views import books_list
from .genre_views import GenreCreateView, GenreListView


app_name = 'books'

urlpatterns = [
    path('', books_list, name='books-list'),
    path('genre/', GenreListView.as_view(), name='books-genre-list'),
    path('genre/create/', GenreCreateView.as_view(), name='books-create-genre'),
]
