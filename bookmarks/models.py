from django.db import models
from django_extensions.db.models import TimeStampedModel

from taggit.managers import TaggableManager


class BookMark(TimeStampedModel):
    name = models.CharField(unique=True, max_length=50)
    url = models.URLField(unique=True)
    description = models.TextField(null=True)

    tags = TaggableManager()
