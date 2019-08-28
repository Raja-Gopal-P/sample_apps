from django.shortcuts import render
from django.views.generic import ListView
from .models import Page


class PagesListView(ListView):
    context_object_name = 'pages'
    model = Page
    template_name = 'pages/pages-list.html'
