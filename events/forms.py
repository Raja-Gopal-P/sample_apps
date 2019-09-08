from django.forms import ModelForm, DateField

from .models import Event, EventTiming


class EventCreationForm(ModelForm):

    date = DateField(help_text='Enter date in format: yyyy-mm-dd')

    class Meta:
        model = Event
        fields = [
            'title',
            'date',
            'full_day_event',
            'place',
            'tags',
        ]


class EventTimingCreationForm(ModelForm):

    class Meta:
        model = EventTiming
        fields = [
            'start_time',
            'end_time',
        ]