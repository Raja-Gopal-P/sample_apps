from django.forms import ModelForm

from .models import Book


class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'authors',
            'publisher',
            'isbn',
            'pages',
            'cover_image',
            'published_date',
            'genre',
            'description',
        ]
