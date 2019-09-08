from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from .models import Book
from .book_forms import BookCreateForm


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/books-list.html'


class BookCreateView(CreateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'books/books-create-book.html'
    success_url = reverse_lazy('books:books-list')
