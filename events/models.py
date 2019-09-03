from django_extensions.db.models import TimeStampedModel
from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

from places.models import Place


class Event(TimeStampedModel):

    title = models.CharField(max_length=60)
    date = models.DateField()
    full_day_event = models.BooleanField(default=False)
    tags = TaggableManager()

    place = models.ForeignKey(to=Place, on_delete=models.CASCADE, related_name='events')
    created_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('title', 'date'), name='unique_event'),
        ]
        ordering = ('date',)

    def __str__(self):
        return '{event_name} - {event_day}'.format(event_name=self.title, event_day=self.date)


class EventTiming(models.Model):

    event = models.ForeignKey(to=Event, on_delete=models.CASCADE, related_name='event_timings')
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('event', 'start_time', 'end_time'), name='unique_time_interval'),
            models.CheckConstraint(check=models.Q(start_time__lt=models.F('end_time')), name='valid_time_interval'),
        ]
        ordering = ('start_time', 'end_time',)
