from django.urls import path

from .views import bookmarks_filter, BookmarkDeleteView, BookmarkCreateView, bookmarks_sorted_filter, \
    BookmarkUpdateView, BookmarkAddTagView

app_name = 'bookmarks'

urlpatterns = [
    path('', bookmarks_filter, name='bookmarks-index-view'),
    path('sort-by-name/', bookmarks_sorted_filter, name='bookmarks-sorted-view'),
    path('<int:id>/delete/', BookmarkDeleteView.as_view(), name='bookmark-delete-view'),
    path('<int:id>/update/', BookmarkUpdateView.as_view(), name='bookmark-update-view'),
    path('<int:id>/tags/', BookmarkAddTagView.as_view(), name='bookmark-add-tag-view'),
    path('create/', BookmarkCreateView.as_view(), name='bookmarks-create-view'),
]
