# Generated by Django 4.2.6 on 2023-11-05 04:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0008_goal_date_added_alter_goal_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 5, 4, 13, 32, 781115, tzinfo=datetime.timezone.utc)),
        ),
    ]
