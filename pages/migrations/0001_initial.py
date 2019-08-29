# Generated by Django 2.2.4 on 2019-08-29 10:21

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('content_html', models.CharField(max_length=4000)),
                ('ordering', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'ordering': ('ordering',),
                'get_latest_by': 'modified',
            },
        ),
    ]
