# Generated by Django 4.2.4 on 2023-08-17 00:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_journey_station_stationorder_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='luggage_weight',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='booking',
            name='number_of_passengers',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
