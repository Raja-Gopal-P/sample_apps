from django_filters.rest_framework import FilterSet, CharFilter

from .models import BookMark


class BookmarkNameFilter(FilterSet):

    filter_by = CharFilter(lookup_expr='contains', field_name='name')

    class Meta:
        model = BookMark
        fields = ['filter_by']
