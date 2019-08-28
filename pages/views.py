from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy

from .models import Page


class PagesListView(ListView):
    context_object_name = 'pages'
    model = Page
    template_name = 'pages/pages-list.html'


class PageCreationView(CreateView):
    success_url = reverse_lazy('pages:pages-list')
    model = Page
    fields = ('title', 'slug', 'content_html', 'ordering',)
    template_name = 'pages/create-page.html'


class PageUpdateView(UpdateView):
    success_url = reverse_lazy('pages:pages-list')
    model = Page
    fields = ('title', 'slug', 'content_html', 'ordering',)
    template_name = 'pages/edit-page.html'
    slug_url_kwarg = 'slug'


class PageView(DetailView):
    model = Page
    context_object_name = 'page'
    slug_url_kwarg = 'slug'

    template_name = 'pages/page-view.html'


class PageDeleteView(DeleteView):
    model = Page
    slug_url_kwarg = 'slug'
    context_object_name = 'page'

    template_name = 'pages/delete-page.html'
    success_url = reverse_lazy('pages:pages-list')
