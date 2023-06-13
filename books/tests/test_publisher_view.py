from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Publisher
from ..publisher_views import PublisherCreateView, PublisherListView, PublisherUpdateView, PublisherDeleteView


class PublisherCreateViewTest(TestCase):

    def setUp(self):
        self.publisher = Publisher.objects.create(name='name', address='address', email='email@email.com', 
                                            phone='+91-123456789')
        self.url = reverse('books:books-create-publisher')

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, PublisherCreateView)

    def test_success_redirect(self):
        name = 'name2'
        response = self.client.post(self.url, data={'name': name,
                                                    'address': 'address',
                                                    'email': 'email1@email.com',
                                                    'phone': '+91-12345678',
                                                    })

        self.assertRedirects(response, reverse('books:books-publisher-list'))
        self.assertTrue(Publisher.objects.filter(name=name))

    def test_failure_response(self):
        name = 'name2'
        response = self.client.post(self.url, data={'name': self.publisher.name,
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


class PublisherListViewTest(TestCase):

    def setUp(self):
        self.url = reverse('books:books-publisher-list')

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, PublisherListView)

    def test_response(self):
        publisher1 = Publisher.objects.create(name='name1', address='address', email='email1', phone='phone1')
        publisher2 = Publisher.objects.create(name='name2', address='address', email='email2', phone='phone2')
        publisher3 = Publisher.objects.create(name='name3', address='address', email='email3', phone='phone3')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, publisher1.name)
        self.assertContains(response, publisher2.name)
        self.assertContains(response, publisher3.name)


class PublisherUpdateViewTest(TestCase):

    def setUp(self):
        self.publisher = Publisher.objects.create(name='name1', address='address', email='email1', phone='phone1')
        self.url = reverse('books:books-update-publisher', kwargs={'id': self.publisher.id, })

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, PublisherUpdateView)

    def test_success_redirect(self):
        name = 'name2'
        response = self.client.post(self.url, data={'name': name,
                                                    'address': 'address',
                                                    'email': 'email1@email.com',
                                                    'phone': '+91-12345678',
                                                    })

        self.assertRedirects(response, reverse('books:books-publisher-list'))
        self.assertTrue(Publisher.objects.filter(name=name))

    def test_failure_response(self):
        response = self.client.post(self.url, data={'name': '',
                                                    'address': '',
                                                    'email': '',
                                                    'phone': '',
                                                    })

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)

    def test_404(self):
        url = reverse('books:books-update-genre', kwargs={'id': self.publisher.id + 1, })
        response = self.client.post(url, data={'name': 'name',
                                               'address': 'address',
                                               'email': 'email1@email.com',
                                               'phone': '+91-12345678',
                                               })

        self.assertEqual(response.status_code, 404)


class PublisherDeleteViewTest(TestCase):

    def setUp(self):
        self.publisher = Publisher.objects.create(name='name1', address='address', email='email1', phone='phone1')
        self.url = reverse('books:books-delete-publisher', kwargs={'id': self.publisher.id, })

    def test_view_resolve(self):
        view = resolve(self.url)
        self.assertEqual(view.func.view_class, PublisherDeleteView)

    def test_success_redirect(self):
        response = self.client.post(self.url)

        self.assertRedirects(response, reverse('books:books-publisher-list'))
        self.assertFalse(Publisher.objects.filter(id=self.publisher.id))

    def test_404(self):
        url = reverse('books:books-delete-publisher', kwargs={'id': self.publisher.id + 1, })
        response = self.client.post(url)

        self.assertEqual(response.status_code, 404)
