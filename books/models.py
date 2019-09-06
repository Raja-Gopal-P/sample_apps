from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


mobile_number_regex_validator = RegexValidator(regex=r'^\+\d{1,3}-\d{3,15}$',
                                               message=_('Allowed format +(country code)-(number) Ex: +91-1234567890'),
                                               code='invalid')

isbn_regex_validator = RegexValidator(regex=r'^\d([\d-])*\d$',
                                      message=_('Enter valid isbn'),
                                      code='invalid')


class Author(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(validators=[mobile_number_regex_validator.__call__], max_length=18, unique=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(validators=[mobile_number_regex_validator.__call__], max_length=18, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    type = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.type


class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(validators=[isbn_regex_validator.__call__], max_length=15, unique=True)
    pages = models.PositiveSmallIntegerField()
    cover_image = models.ImageField(unique=True)
    description = models.TextField()
    published_date = models.DateField()

    authors = models.ManyToManyField(Author, related_name='books', through='BookAuthor',
                                     through_fields=('book', 'author'))

    publisher = models.ForeignKey(to=Publisher, related_name='publisher', on_delete=models.CASCADE)
    genre = models.ForeignKey(to=Genre, null=True, related_name='genre', on_delete=models.SET_NULL)

    def __str__(self):
        return self.isbn


class BookAuthor(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(name='unique_book_author', fields=('book_id', 'author_id'))
        ]
