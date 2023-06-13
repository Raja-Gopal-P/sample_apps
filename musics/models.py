from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


number_regex_validator = RegexValidator(regex=r'^\d+$',
                                        message=_('Enter valid phone number'),
                                        code='invalid')

mobile_number_regex_validator = RegexValidator(regex=r'^\+\d{1,3}-\d{3,15}$',
                                               message=_('Enter valid phone number'),
                                               code='invalid')


class Genre(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True)

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title


class Label(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        ordering = ('name', )


class Band(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        ordering = ('name', )


class Album(models.Model):
    title = models.CharField(max_length=50, unique=True)
    prefix = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    asin = models.CharField(max_length=15, unique=True, validators=[number_regex_validator, ])
    release_date = models.DateField()
    cover = models.ImageField(upload_to='musics', unique=True)

    genre = models.ManyToManyField(Genre, related_name='albums')

    band = models.ForeignKey(null=True, to=Band, related_name='albums', on_delete=models.SET_NULL)
    label = models.ForeignKey(null=True, to=Label, related_name='albums', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title


class Music(models.Model):
    title = models.CharField(unique=True, max_length=50)
    slug = models.SlugField(unique=True)

    album = models.ForeignKey(null=True, to=Album, related_name='musics', on_delete=models.SET_NULL)
    band = models.ForeignKey(null=True, to=Band, related_name='musics', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('title', )
