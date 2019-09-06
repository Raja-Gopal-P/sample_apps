from django.forms import ModelForm, CharField

from .models import Author


class AuthorCreateForm(ModelForm):

    phone = CharField(help_text='Allowed format +(country code)-(number) Ex: +91-1234567890')

    class Meta:
        model = Author
        fields = ['name', 'address', 'email', 'phone', ]
