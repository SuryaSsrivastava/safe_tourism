# Generated by Django 3.0.8 on 2020-10-05 16:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tourist', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='bookings',
            new_name='booking',
        ),
        migrations.RenameModel(
            old_name='tourist_places',
            new_name='tourist_place',
        ),
    ]
