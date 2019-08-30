from django_filters import FilterSet

from .models import Place


class PlacesCityFilter(FilterSet):

    class Meta:
        model = Place
        fields = ['city']
