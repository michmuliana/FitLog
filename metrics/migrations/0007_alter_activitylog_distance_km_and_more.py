# Generated by Django 4.2.6 on 2023-11-04 02:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0006_alter_activitylog_description_alter_goal_distance_km_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylog',
            name='distance_km',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='activitylog',
            name='elapsed_seconds',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='activitylog',
            name='name',
            field=models.TextField(choices=[('run', 'Run'), ('bike', 'Bike'), ('swim', 'Swim')]),
        ),
    ]
