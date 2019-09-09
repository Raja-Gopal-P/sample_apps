from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


mobile_number_regex_validator = RegexValidator(regex=r'^\+\d{1,3}-\d{3,15}$',
                                               message=_('Enter valid phone number'),
                                               code='invalid')

number_regex_validator = RegexValidator(regex=r'^\d+$',
                                               message=_('Enter valid phone number'),
                                               code='invalid')


class Studio(models.Model):
    title = models.CharField(max_length=60, unique=True)
    prefix = models.CharField(max_length=20)
    slug = models.SlugField(max_length=80, unique=True)
    website = models.URLField(unique=True)

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True)

    def __str__(self):
        return self.title


class Director(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    phone_number = models.CharField(validators=[mobile_number_regex_validator, ], max_length=18, unique=True)
    birth_date = models.DateField()
    website = models.URLField(unique=True)
    gender = models.PositiveSmallIntegerField(choices=(
        (1, 'male'),
        (2, 'female'),
    ))

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('first_name', 'middle_name', 'last_name'), name='unique_name'),
        ]

    def __str__(self):
        return '{first} {middle} {last}'.format(first=self.first_name, middle=self.middle_name, last=self.last_name)


class Movie(models.Model):
    title = models.CharField(max_length=60, unique=True)
    prefix = models.CharField(max_length=20)
    sub_title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=80, unique=True)
    released_date = models.DateField()
    cover_image = models.ImageField(unique=True, upload_to='movies')
    review = models.FloatField(default=5)
    asin = models.CharField(max_length=15, unique=True, validators=[number_regex_validator, ])

    studio = models.ForeignKey(to=Studio, related_name='movies', on_delete=models.SET_NULL, null=True)

    directors = models.ManyToManyField(to=Director, related_name='movies')
    genres = models.ManyToManyField(to=Genre, related_name='movies')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.amazon_url = 'http://www.amazon.in/s?k={}'.format(self.asin)
