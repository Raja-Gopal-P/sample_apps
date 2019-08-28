from django.views.generic import ListView, CreateView
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
