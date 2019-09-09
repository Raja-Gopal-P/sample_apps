from django.forms import ModelForm, CharField

from .models import Publisher


class PublisherCreateForm(ModelForm):

    phone = CharField(help_text='Allowed format +(country code)-(number) Ex: +91-1234567890')

    class Meta:
        model = Publisher
        fields = ['name', 'address', 'email', 'phone', ]


class PublisherUpdateForm(ModelForm):

    phone = CharField(help_text='Allowed format +(country code)-(number) Ex: +91-1234567890')

    class Meta:
        model = Publisher
        fields = ['name', 'address', 'email', 'phone', ]
