import json
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.views.generic import View
from django.db import connection, transaction
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from datetime import datetime
from django.utils import timezone

from .models import User, ActivityLog, Goal
from .serializer import UserSerializer, ActivityLogSerializer, GoalSerializer

# API Endpoint to make get, post, put and patch
class ActivityLogView(View):

    # Retrieve all user activity log history
    def get(self, request, *args, **kwargs):
        activityLogModel = ActivityLog.objects.all()
        serializeActivityLog = ActivityLogSerializer(activityLogModel, many=True)
        # self.totalHoursExercised()
        return HttpResponse(json.dumps(serializeActivityLog.data))
    
    # Get data when the user submit an activity log form
    def post(self, request):
        serializeActivityLog = ActivityLogSerializer(data=request.data)
        if serializeActivityLog.is_valid():
            serializeActivityLog.save()
            return HttpResponse(serializeActivityLog.data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(serializeActivityLog.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Home: Aggregate the hours exercised between a given start and end date from the activity log table
    def totalHoursExercised(self):
        startDate = f"\'{datetime.now().year}-01-01\'"
        endDate = f"\'{datetime.now().year}-12-31\'"
        sqlStatement = f'''
            SELECT SUM(elapsed_seconds) as total_exercise_time 
            FROM metrics_activitylog 
            WHERE datetime between {startDate} and {endDate};
        '''
        cursor = connection.cursor()
        cursor.execute(sqlStatement)
        totalHours = cursor.fetchone()[0]
        print(str(totalHours))
        return HttpResponse(totalHours)
        
class GoalView(View):
    # Retrieve all logged goal by the user
    def get(self, request, *args, **kwargs):
        goalModel = Goal.objects.all()
        serializeGoal = GoalSerializer(goalModel, many=True)
        return HttpResponse(json.dumps(serializeGoal.data))
    
    # Get data when the user submit a goal form
    def post(self, request):
        serializeGoal = GoalSerializer(data=request.data)
        if serializeGoal.is_valid():
            serializeGoal.save()
            return HttpResponse(serializeGoal.data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(serializeGoal.errors, status=status.HTTP_400_BAD_REQUEST)

# CalendarView, ActivityLogView, FAQView