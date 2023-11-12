# Generated by Django 4.2.6 on 2023-11-05 04:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0009_alter_goal_date_added'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activitylog',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='goal',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='goal',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 5, 4, 21, 24, 821353, tzinfo=datetime.timezone.utc)),
        ),
    ]
