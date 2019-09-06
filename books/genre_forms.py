from django.forms import ModelForm, CharField

from .models import Genre


class GenreCreateForm(ModelForm):

    type = CharField(label='Genre Type', help_text='Unique field')

    class Meta:
        model = Genre
        fields = ['type', ]
