from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, reverse, redirect
from django.db import transaction

import re

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


def reorder_page(request, **kwargs):
    context = {}

    if request.method == 'POST':
        page_order_dict = {}

        items_order = request.POST.get('items_order')
        if items_order is None:
            context['op_fail'] = 'Invalid Format'
        elif items_order:
            ordered_pages = items_order.split('&')

            for order, page in enumerate(ordered_pages):
                if re.match(r'^(item\[\]=\d+)$', page):
                    page_id = int(page.split('=')[1])
                    if page_id in page_order_dict:
                        context['op_fail'] = 'Duplicate Entry Found'
                        page_order_dict = {}
                        break
                    page_order_dict[page_id] = order
                else:
                    context['op_fail'] = 'Invalid Format'
                    page_order_dict = {}
                    break

        if 'op_fail' not in context:
            valid_op = True
            pages = Page.objects.all()
            for page in pages:
                if page.id in page_order_dict:
                    if not valid_op:
                        context['op_fail'] = 'Invalid Format'
                        break
                else:
                    valid_op = False
            else:
                with transaction.atomic():
                    pages = Page.objects.select_for_update()
                    for page in pages:
                        if page.id in page_order_dict:
                            page.ordering = page_order_dict[page.id]
                        else:
                            page.ordering = len(page_order_dict)
                        page.save()
                    else:
                        return redirect(reverse('pages:pages-list'))

        pages = Page.objects.all()
        context['pages'] = pages
        return render(request, 'Pages/reorder.html', context)

    else:
        pages = Page.objects.all()
        context['pages'] = pages
        return render(request, 'Pages/reorder.html', context)

