from django.db import models
from django.contrib.gis.db.models import PointField
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


mobile_number_regex_validator = RegexValidator(regex=r'^\+\d{1,3}-\d{3,15}$',
                                               message=_('Allowed format +(country code)-(number) Ex: +91-1234567890'),
                                               code='invalid')
types_regex_validator = RegexValidator(regex=r'^[a-zA-Z \-_,]*$')


def tags_validator(value):
    if not re.match(r'^([a-zA-Z_,])*$', value):
        raise ValidationError(
            _('Alphabets, underscore and comma only'),)


class City(models.Model):
    city_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.city_name


class Place(models.Model):

    title = models.CharField(max_length=50, unique=True)
    location = PointField()
    description = models.CharField(max_length=1000, null=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(validators=[mobile_number_regex_validator.__call__], max_length=18, unique=True)
    city = models.ForeignKey(to=City, on_delete=models.CASCADE, related_name='places')
    types = models.CharField(validators=[types_regex_validator.__call__], max_length=100)
    tags = models.CharField(validators=[tags_validator], max_length=100, default=None, blank=True)
