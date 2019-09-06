from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Author
from .author_forms import AuthorCreateForm


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm

    template_name = 'books/author-create-view.html'
    success_url = reverse_lazy('books:books-genre-list')
