# Generated by Django 2.2.4 on 2019-09-09 06:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0012_auto_20190909_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='phone',
            field=models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator.__call__]),
        ),
        migrations.AlterField(
            model_name='place',
            name='types',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator.__call__]),
        ),
    ]
