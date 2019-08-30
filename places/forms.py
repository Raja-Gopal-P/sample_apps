from django.forms.models import ModelForm
from django import forms

from leaflet.forms.fields import PointField

from .models import Place


class CreatePlaceForm(ModelForm):

    location = PointField()
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 5,
                'placeholder': 'Short description about the place',
            }
        ),
        max_length=1000,
        help_text='Maximum 1000 characters'
    )
    address = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 5,
            }
        ),
        max_length=200,
        help_text='Maximum 200 characters'
    )

    class Meta:
        model = Place
        fields = ('title',
                  'location',
                  'description',
                  'address',
                  'phone',
                  'city',
                  'types',
                  'tags',
                  )
