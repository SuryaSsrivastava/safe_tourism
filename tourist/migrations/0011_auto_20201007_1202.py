# Generated by Django 3.0.8 on 2020-10-07 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0010_auto_20201007_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booking_id',
            new_name='id',
        ),
    ]
