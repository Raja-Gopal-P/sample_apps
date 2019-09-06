from django.test import TestCase
from django.db import models
from django.db.utils import IntegrityError

from datetime import date

from ..models import Author, Publisher, Genre, Book, BookAuthor


class AuthorModelTest(TestCase):

    def test_fields(self):
        self.assertEqual(Author._meta.get_field('name').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Author._meta.get_field('address').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Author._meta.get_field('email').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Author._meta.get_field('phone').get_internal_type(), models.CharField.__name__)

    def test_unique_email_field(self):
        with self.assertRaises(IntegrityError):
            Author.objects.create(name='name', address='address', email='email', phone='phone1')
            Author.objects.create(name='name', address='address', email='email', phone='phone2')

    def test_unique_phone_field(self):
        with self.assertRaises(IntegrityError):
            Author.objects.create(name='name', address='address', email='email1', phone='phone')
            Author.objects.create(name='name', address='address', email='email2', phone='phone')


class PublisherModelTest(TestCase):

    def test_fields(self):
        self.assertEqual(Publisher._meta.get_field('name').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Publisher._meta.get_field('address').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Publisher._meta.get_field('email').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Publisher._meta.get_field('phone').get_internal_type(), models.CharField.__name__)

    def test_unique_email_field(self):
        with self.assertRaises(IntegrityError):
            Publisher.objects.create(name='name', address='address', email='email', phone='phone1')
            Publisher.objects.create(name='name', address='address', email='email', phone='phone2')

    def test_unique_phone_field(self):
        with self.assertRaises(IntegrityError):
            Publisher.objects.create(name='name', address='address', email='email1', phone='phone')
            Publisher.objects.create(name='name', address='address', email='email2', phone='phone')


class GenreModelTest(TestCase):

    def test_fields(self):
        self.assertEqual(Genre._meta.get_field('type').get_internal_type(), models.CharField.__name__)

    def test_unique_type_field(self):
        with self.assertRaises(IntegrityError):
            Genre.objects.create(type='type')
            Genre.objects.create(type='type')


class BookModelTest(TestCase):

    def setUp(self):
        self.genre = Genre.objects.create(type='type1')
        self.publisher = Publisher.objects.create(name='name', address='address', email='email1', phone='phone')

        self.book = Book.objects.create(title='title', isbn='isbn', pages=3, cover_image='img1', description='desc',
                                        published_date=date(year=2019, month=9, day=6), publisher=self.publisher,
                                        genre=self.genre)

    def test_fields(self):
        self.assertEqual(Book._meta.get_field('title').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Book._meta.get_field('isbn').get_internal_type(), models.CharField.__name__)
        self.assertEqual(Book._meta.get_field('pages').get_internal_type(), models.PositiveSmallIntegerField.__name__)
        self.assertEqual(Book._meta.get_field('cover_image').get_internal_type(), models.FileField.__name__)
        self.assertEqual(Book._meta.get_field('description').get_internal_type(), models.TextField.__name__)
        self.assertEqual(Book._meta.get_field('published_date').get_internal_type(), models.DateField.__name__)
        self.assertEqual(Book._meta.get_field('publisher').get_internal_type(), models.ForeignKey.__name__)
        self.assertEqual(Book._meta.get_field('genre').get_internal_type(), models.ForeignKey.__name__)
        self.assertEqual(Book._meta.get_field('authors').get_internal_type(), models.ManyToManyField.__name__)

    def test_unique_isbn_field(self):
        with self.assertRaises(IntegrityError):
            Book.objects.create(title='title', isbn=self.book.isbn, pages=3, cover_image='img1', description='desc',
                                published_date=date(year=2019, month=9, day=6), publisher=self.publisher,
                                genre=self.genre)

    def test_unique_cover_image_field(self):
        with self.assertRaises(IntegrityError):
            Book.objects.create(title='title', isbn=self.book.isbn+'_unique', pages=3,
                                cover_image=self.book.cover_image, description='desc',
                                published_date=date(year=2019, month=9, day=6), publisher=self.publisher,
                                genre=self.genre)

    def test_genre_reference_delete(self):
        self.genre.delete()
        self.book.refresh_from_db()
        self.assertFalse(self.book.genre)

    def test_publisher_reference_delete(self):
        self.publisher.delete()
        self.assertFalse(Book.objects.exists())


class BookAuthorModelTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(type='type1')
        self.publisher = Publisher.objects.create(name='name', address='address', email='email1', phone='phone')
        self.author1 = Author.objects.create(name='name', address='address', email='email1', phone='phone1')
        self.author2 = Author.objects.create(name='name', address='address', email='email2', phone='phone2')

        self.book = Book.objects.create(title='title', isbn='isbn1', pages=3, cover_image='img1', description='desc',
                                        published_date=date(year=2019, month=9, day=6), publisher=self.publisher,
                                        genre=self.genre)
        self.book.authors.add(self.author1)
        self.book.authors.add(self.author2)

        self.book2 = Book.objects.create(title='title', isbn='isbn2', pages=3, cover_image='img2', description='desc',
                                         published_date=date(year=2019, month=9, day=6), publisher=self.publisher,
                                         genre=self.genre)
        self.book2.authors.add(self.author1)

    def test_author_reference_delete(self):
        self.author1.delete()
        self.assertFalse(self.book2.authors.all())

    def test_book_reference_delete(self):
        book_id = self.book.id
        self.book.delete()

        self.assertFalse(BookAuthor.objects.filter(book_id=book_id))
