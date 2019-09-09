# Generated by Django 2.2.4 on 2019-09-08 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='director',
            constraint=models.UniqueConstraint(fields=('first_name', 'middle_name', 'last_name'), name='unique_name'),
        ),
    ]