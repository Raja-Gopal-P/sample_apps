from django.test import TestCase
from django.urls import resolve, reverse

from datetime import date

from ..models import Publisher, Book, Genre
from ..book_views import BookCreateView, BookListView, BookUpdateView


class BookCreateViewTest(TestCase):

    def test_view_resolve(self):
        url = reverse('books:books-create-book')
        view = resolve(url)
        self.assertEqual(view.func.view_class, BookCreateView)


class BookListViewTest(TestCase):

    def setUp(self):
        publisher = Publisher.objects.create(name='name', address='address', email='email1', phone='phone')
        genre = Genre.objects.create(type='type')
        self.book = Book.objects.create(title='title', isbn='isbn', pages=3, cover_image='img1', description='desc',
                                        published_date=date(year=2019, month=9, day=6), publisher=publisher,
                                        genre=genre)

        self.url = reverse('books:books-list')

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, BookListView)

    def test_response(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('books'))


class BookUpdateViewTest(TestCase):

    def test_view_resolve(self):
        publisher = Publisher.objects.create(name='name', address='address', email='email1', phone='phone')
        genre = Genre.objects.create(type='type')
        book = Book.objects.create(title='title', isbn='isbn', pages=3, cover_image='img1', description='desc',
                                   published_date=date(year=2019, month=9, day=6), publisher=publisher,
                                   genre=genre)
        url = reverse('books:books-edit-book', kwargs={'id': book.id})
        view = resolve(url)
        self.assertEqual(view.func.view_class, BookUpdateView)
