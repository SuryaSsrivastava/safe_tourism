# Generated by Django 3.0.8 on 2020-10-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0004_auto_20201006_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tourist_place',
            name='place_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
