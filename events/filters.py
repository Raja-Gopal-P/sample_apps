from django_filters import FilterSet, DateFilter, NumberFilter

from .models import Event


class EventsDateFilter(FilterSet):

    date = DateFilter(field_name='date', help_text='Enter date in format: yyyy-mm-dd.')

    class Meta:
        model = Event
        fields = ['date']


class EventsMonthFilter(FilterSet):

    month = NumberFilter(lookup_expr='month', field_name='date', help_text='Range is [1, 12]',
                         min_value=1, max_value=12, label='Month')

    class Meta:
        model = Event
        fields = ['month']


class EventsYearFilter(FilterSet):

    year = NumberFilter(lookup_expr='year', field_name='date', label='Year', help_text='Range is [1, 9999]',
                        min_value=1, max_value=9999)

    class Meta:
        model = Event
        fields = ['year']
