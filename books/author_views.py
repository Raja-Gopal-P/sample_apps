from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from .models import Author
from .author_forms import AuthorCreateForm


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm

    template_name = 'books/author-create-view.html'
    success_url = reverse_lazy('books:books-author-list')


class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = 'books/author-list-view.html'
