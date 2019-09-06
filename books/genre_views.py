from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy

from .models import Genre
from .genre_forms import GenreCreateForm, GenreUpdateForm


class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreCreateForm

    template_name = 'books/genre-create-view.html'
    success_url = reverse_lazy('books:books-genre-list')


class GenreListView(ListView):
    model = Genre
    context_object_name = 'genres'
    template_name = 'books/genre-list-view.html'


class GenreUpdateView(UpdateView):
    model = Genre
    pk_url_kwarg = 'id'
    context_object_name = 'genre'
    form_class = GenreUpdateForm

    template_name = 'books/genre-edit-view.html'
    success_url = reverse_lazy('books:books-genre-list')
