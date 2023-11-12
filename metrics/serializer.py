from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User 
        fields = (
            'user_name'
        )
        
class ActivityLogSerializer(ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = (
            'name', 
            'description',
            'datetime',
            'elapsed_seconds',
            'distance_km',
            'user'
        )

class GoalSerializer(ModelSerializer):
    class Meta:
        model = Goal
        fields = (
            'activity',
            'frequency',
            'type',
            'durations_seconds',
            'distance_km',
            'user',
            'date_added'
        )