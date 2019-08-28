from django_extensions.db.models import TimeStampedModel
from django.db import models


class Page(TimeStampedModel):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    content_html = models.CharField(max_length=4000)
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        get_latest_by = 'modified'
        ordering = ('ordering',)
