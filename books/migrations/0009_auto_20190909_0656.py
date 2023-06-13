# Generated by Django 2.2.4 on 2019-09-09 06:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20190909_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='phone',
            field=models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator.__call__]),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator.__call__]),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='phone',
            field=models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator.__call__]),
        ),
    ]
