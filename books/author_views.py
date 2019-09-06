from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy

from .models import Author
from .author_forms import AuthorCreateForm, AuthorUpdateForm


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm

    template_name = 'books/author-create-view.html'
    success_url = reverse_lazy('books:books-author-list')


class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = 'books/author-list-view.html'


class AuthorUpdateView(UpdateView):
    model = Author
    pk_url_kwarg = 'id'
    context_object_name = 'author'
    form_class = AuthorUpdateForm

    template_name = 'books/author-edit-view.html'
    success_url = reverse_lazy('books:books-author-list')
