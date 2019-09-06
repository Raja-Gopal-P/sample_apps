from django.urls import path

from .book_views import books_list
from .genre_views import GenreCreateView, GenreListView, GenreUpdateView, GenreDeleteView
from .author_views import AuthorCreateView, AuthorListView, AuthorUpdateView, AuthorDeleteView
from .publisher_views import PublisherCreateView, PublisherListView, PublisherUpdateView, PublisherDeleteView


app_name = 'books'

urlpatterns = [
    path('', books_list, name='books-list'),
    path('genre/', GenreListView.as_view(), name='books-genre-list'),
    path('genre/create/', GenreCreateView.as_view(), name='books-create-genre'),
    path('genre/<int:id>/edit/', GenreUpdateView.as_view(), name='books-update-genre'),
    path('genre/<int:id>/delete/', GenreDeleteView.as_view(), name='books-delete-genre'),
    path('author/', AuthorListView.as_view(), name='books-author-list'),
    path('author/create/', AuthorCreateView.as_view(), name='books-create-author'),
    path('author/<int:id>/edit/', AuthorUpdateView.as_view(), name='books-update-author'),
    path('author/<int:id>/delete/', AuthorDeleteView.as_view(), name='books-delete-author'),
    path('publisher/', PublisherListView.as_view(), name='books-publisher-list'),
    path('publisher/create/', PublisherCreateView.as_view(), name='books-create-publisher'),
    path('publisher/<int:id>/edit/', PublisherUpdateView.as_view(), name='books-update-publisher'),
    path('publisher/<int:id>/delete/', PublisherDeleteView.as_view(), name='books-delete-publisher'),
]
