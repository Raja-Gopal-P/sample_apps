from django.views.generic import DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import BookMark
from .filters import BookmarkNameFilter


def bookmarks_filter(request):
    bookmarks = BookMark.objects.all()
    filtered_bookmarks = BookmarkNameFilter(request.GET, queryset=bookmarks)

    return render(request, 'bookmarks/bookmarks-list.html', {'bookmarks': filtered_bookmarks.qs,
                                                             'form': filtered_bookmarks.form,
                                                             })


class BookmarkDeleteView(DeleteView):
    model = BookMark
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('bookmarks:bookmarks-index-view')
    http_method_names = ['post']
