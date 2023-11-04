# Generated by Django 4.2.6 on 2023-11-04 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0004_rename_goals_goal_alter_user_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylog',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='goal',
            name='distance_km',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='goal',
            name='durations_seconds',
            field=models.IntegerField(null=True),
        ),
    ]
