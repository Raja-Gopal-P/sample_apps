from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Author
from ..author_views import AuthorCreateView, AuthorListView, AuthorUpdateView, AuthorDeleteView


class AuthorCreateViewTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(name='name', address='address', email='email@email.com', 
                                            phone='+91-123456789')
        self.url = reverse('books:books-create-author')

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, AuthorCreateView)

    def test_success_redirect(self):
        name = 'name2'
        response = self.client.post(self.url, data={'name': name,
                                                    'address': 'address',
                                                    'email': 'email1@email.com',
                                                    'phone': '+91-12345678',
                                                    })

        self.assertRedirects(response, reverse('books:books-author-list'))
        self.assertTrue(Author.objects.filter(name=name))

    def test_failure_response(self):
        name = 'name2'
        response = self.client.post(self.url, data={'name': self.author.name,
                                                    'address': 'address',
                                                    'email': 'email1@email.com',
                                                    'phone': '+91-12345678',
                                                    })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)

        response = self.client.post(self.url, data={'name': name,
                                                    'address': 'address',
                                                    'email': 'email@email.com',
                                                    'phone': '+91-12345678',
                                                    })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)

        response = self.client.post(self.url, data={'name': name,
                                                    'address': 'address',
                                                    'email': 'email1@email.com',
                                                    'phone': '+91-123456789',
                                                    })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)

        response = self.client.post(self.url, data={'name': '',
                                                    'address': '',
                                                    'email': '',
                                                    'phone': '',
                                                    })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)


class AuthorListViewTest(TestCase):

    def setUp(self):
        self.url = reverse('books:books-author-list')

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, AuthorListView)

    def test_response(self):
        author1 = Author.objects.create(name='name1', address='address', email='email1', phone='phone1')
        author2 = Author.objects.create(name='name2', address='address', email='email2', phone='phone2')
        author3 = Author.objects.create(name='name3', address='address', email='email3', phone='phone3')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, author1.name)
        self.assertContains(response, author2.name)
        self.assertContains(response, author3.name)


class AuthorUpdateViewTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(name='name1', address='address', email='email1', phone='phone1')
        self.url = reverse('books:books-update-author', kwargs={'id': self.author.id, })

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, AuthorUpdateView)

    def test_success_redirect(self):
        name = 'name2'
        response = self.client.post(self.url, data={'name': name,
                                                    'address': 'address',
                                                    'email': 'email1@email.com',
                                                    'phone': '+91-12345678',
                                                    })

        self.assertRedirects(response, reverse('books:books-author-list'))
        self.assertTrue(Author.objects.filter(name=name))

    def test_failure_response(self):
        response = self.client.post(self.url, data={'name': '',
                                                    'address': '',
                                                    'email': '',
                                                    'phone': '',
                                                    })

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)

    def test_404(self):
        url = reverse('books:books-update-genre', kwargs={'id': self.author.id + 1, })
        response = self.client.post(url, data={'name': 'name',
                                               'address': 'address',
                                               'email': 'email1@email.com',
                                               'phone': '+91-12345678',
                                               })

        self.assertEqual(response.status_code, 404)


class AuthorDeleteViewTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(name='name1', address='address', email='email1', phone='phone1')
        self.url = reverse('books:books-delete-author', kwargs={'id': self.author.id, })

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, AuthorDeleteView)

    def test_success_redirect(self):
        response = self.client.post(self.url)

        self.assertRedirects(response, reverse('books:books-author-list'))
        self.assertFalse(Author.objects.filter(id=self.author.id))

    def test_404(self):
        url = reverse('books:books-delete-author', kwargs={'id': self.author.id + 1, })
        response = self.client.post(url)

        self.assertEqual(response.status_code, 404)
