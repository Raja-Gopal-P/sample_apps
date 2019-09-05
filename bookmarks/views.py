from django.views.generic import DeleteView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import BookMark
from .filters import BookmarkNameFilter
from .forms import BookmarkCreationForm


def bookmarks_filter(request):
    bookmarks = BookMark.objects.all()
    filtered_bookmarks = BookmarkNameFilter(request.GET, queryset=bookmarks)

    return render(request, 'bookmarks/bookmarks-list.html', {'bookmarks': filtered_bookmarks.qs,
                                                             'form': filtered_bookmarks.form,
                                                             })


def bookmarks_sorted_filter(request):
    bookmarks = BookMark.objects.all().order_by('name')
    filtered_bookmarks = BookmarkNameFilter(request.GET, queryset=bookmarks)

    return render(request, 'bookmarks/bookmarks-sort-by-name-list.html', {'bookmarks': filtered_bookmarks.qs,
                                                                          'form': filtered_bookmarks.form,
                                                                          })


class BookmarkCreateView(CreateView):
    model = BookMark
    template_name = 'bookmarks/bookmarks-create-view.html'
    form_class = BookmarkCreationForm
    success_url = reverse_lazy('bookmarks:bookmarks-index-view')

    def form_invalid(self, form):
        return redirect(self.success_url)


class BookmarkDeleteView(DeleteView):
    model = BookMark
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('bookmarks:bookmarks-index-view')
    http_method_names = ['post']


class BookmarkUpdateView(UpdateView):
    model = BookMark
    pk_url_kwarg = 'id'
    context_object_name = 'bookmark'
    template_name = 'bookmarks/bookmarks-update-view.html'
    form_class = BookmarkCreationForm
    success_url = reverse_lazy('bookmarks:bookmarks-index-view')

    def form_invalid(self, form):
        return redirect(self.success_url)
