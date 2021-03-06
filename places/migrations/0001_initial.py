# Generated by Django 2.2.4 on 2019-08-29 10:19

import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import places.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator.__call__])),
                ('types', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator.__call__])),
                ('tags', models.CharField(blank=True, default=None, max_length=100, validators=[places.models.tags_validator])),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='places.City')),
            ],
        ),
    ]
