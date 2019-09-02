# Generated by Django 2.2.4 on 2019-09-02 03:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20190829_1103'),
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
