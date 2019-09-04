from django.urls import path

from .views import bookmarks_filter

app_name = 'bookmarks'

urlpatterns = [
    path('', bookmarks_filter, name='bookmarks-index-view'),
]
