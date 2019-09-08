from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Publisher
from .publisher_forms import PublisherCreateForm, PublisherUpdateForm


class PublisherCreateView(CreateView):
    model = Publisher
    form_class = PublisherCreateForm

    template_name = 'books/publisher-create-view.html'
    success_url = reverse_lazy('books:books-publisher-list')


class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'publishers'
    template_name = 'books/publisher-list-view.html'


class PublisherUpdateView(UpdateView):
    model = Publisher
    pk_url_kwarg = 'id'
    context_object_name = 'publisher'
    form_class = PublisherUpdateForm

    template_name = 'books/publisher-edit-view.html'
    success_url = reverse_lazy('books:books-publisher-list')


class PublisherDeleteView(DeleteView):
    model = Publisher
    pk_url_kwarg = 'id'

    http_method_names = ['post', ]
    success_url = reverse_lazy('books:books-publisher-list')
