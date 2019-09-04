from django.views.generic import TemplateView
from django.shortcuts import render

from .models import BookMark
from .filters import BookmarkNameFilter


def bookmarks_filter(request):
    bookmarks = BookMark.objects.all()
    filtered_bookmarks = BookmarkNameFilter(request.GET, queryset=bookmarks)

    return render(request, 'bookmarks/bookmarks-list.html', {'bookmarks': filtered_bookmarks.qs,
                                                             'form': filtered_bookmarks.form,
                                                             })
