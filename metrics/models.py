from django.db import models
from django.core.validators import MinValueValidator
import datetime
import time
from django.utils import timezone


class User(models.Model):
    user_name = models.TextField(null=False)
    
class ActivityLog(models.Model):
    name = models.TextField(
        null=False,
            choices=(
            ("run", "Run"),
            ("bike", "Bike"),
            ("swim", "Swim"),
        ))
    description = models.TextField(null=True, blank=True)
    datetime = models.DateTimeField(null=False)
    elapsed_seconds = models.PositiveIntegerField(null=False)
    distance_km = models.FloatField(null=False, validators=[MinValueValidator(0.0)])
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=False)
    
class Goal(models.Model):
    activity = models.TextField(
            null=False,
                choices=(
                ("run", "Run"),
                ("bike", "Bike"),
                ("swim", "Swim"),
            )
        )
    frequency = models.TextField(
        null=False,
        choices=(
            ("weekly", "Weekly"),
            ("monthly", "Monthly"),
            ("yearly", "Yearly"),
        ))
    type = models.TextField(
        null=False,
        choices=(
            ("distance", "Distance"),
            ("time", "Time"),
        )
        )
    durations_seconds = models.PositiveIntegerField(null=True, blank=True)
    distance_km = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0)])
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=False)
    date_added = models.DateTimeField(null=False, default=timezone.now())
    
    
    