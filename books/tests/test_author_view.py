from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Author
from ..author_views import AuthorCreateView


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

        self.assertRedirects(response, reverse('books:books-genre-list'))
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
