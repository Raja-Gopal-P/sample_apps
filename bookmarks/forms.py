from django.forms import ModelForm, CharField, Textarea

from .models import BookMark


class BookmarkCreationForm(ModelForm):

    name = CharField(help_text='Unique Name')
    url = CharField(help_text='Unique URL')
    description = CharField(
        widget=Textarea(
            attrs={'rows': 3,
                   'placeholder': 'Description in 150 words', }),
        max_length=150,
    )

    class Meta:
        model = BookMark
        fields = ['name', 'url', 'description', ]
