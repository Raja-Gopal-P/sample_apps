from django.urls import path

from .views import bookmarks_filter, BookmarkDeleteView

app_name = 'bookmarks'

urlpatterns = [
    path('', bookmarks_filter, name='bookmarks-index-view'),
    path('<int:id>/delete/', BookmarkDeleteView.as_view(), name='bookmark-delete-view'),
]
