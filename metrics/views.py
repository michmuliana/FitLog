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
    def get(self, request, *args, **kwargs):
        activityLogModel = ActivityLog.objects.all()
        serializeActivityLog = ActivityLogSerializer(activityLogModel, many=True)
        return HttpResponse(json.dumps(serializeActivityLog.data))
    
    # Get data when the user submit an activity log form
    def post(self, request):
        serializeActivityLog = ActivityLogSerializer(data=request.data)
        if serializeActivityLog.is_valid():
            serializeActivityLog.save()
            return HttpResponse(serializeActivityLog.data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(serializeActivityLog.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # Retrieve all user activity log history
    def activityLogHistory(self):
        return
        

        
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

class SummaryView(View):
    def __init__(self):
        self.startDate = f"\'{datetime.now().year}-01-01\'"
        self.endDate = f"\'{datetime.now().year}-12-31\'"
        self.runCalories = 60
        self.bikeCalories = 23
        self.swimCalories = 305
    
    def get(self, request, *args, **kwargs):
        self.totalCalories
        return HttpResponse(json.dumps({"totalHoursExercised":self.totalHoursExercised(), "totalDistanceCovered": self.totalDistanceCovered(), "totalCalories": self.totalCalories()}))
    
    # Aggregate the hours exercised between a given start and end date from the activity log table
    def totalHoursExercised(self):
        sqlStatement = f'''
            SELECT SUM(elapsed_seconds) as total_exercise_time 
            FROM metrics_activitylog 
            WHERE datetime between {self.startDate} and {self.endDate};
        '''
        cursor = connection.cursor()
        cursor.execute(sqlStatement)
        totalHours = cursor.fetchone()[0]
        print(f"Total hours exercised: {totalHours}")
        return totalHours
    
    # Aggregate the distance covered between a given start and end date from the activity log table
    def totalDistanceCovered(self):
        sqlStatement = f'''
            SELECT SUM(distance_km) as total_exercise_distance
            FROM metrics_activitylog 
            WHERE datetime between {self.startDate} and {self.endDate};
        '''
        cursor = connection.cursor()
        cursor.execute(sqlStatement)
        totalDistance = cursor.fetchone()[0]
        print(f"Total distance covered: {totalDistance}")
        return totalDistance
    
    # Aggregate calories burned between a given start and end date from the activity log table
    def totalCalories(self):
        sqlStatement = f'''
            SELECT name, SUM(distance_km) as total_exercise_distance
            FROM metrics_activitylog 
            WHERE datetime between {self.startDate} and {self.endDate}
            GROUP BY name
        '''
        cursor = connection.cursor()
        cursor.execute(sqlStatement)
        totalDistance = cursor.fetchall()
        print(totalDistance)
        for activity, distance in totalDistance:
            if activity == 'bike':
                totalBikeCalories = distance*self.bikeCalories
            elif activity == 'run':
                totalRunCalories = distance*self.runCalories
            elif activity == 'swim':
                totalSwimCalories = distance*self.swimCalories
        
        totalCaloriesBurned = totalBikeCalories + totalRunCalories + totalSwimCalories
        return totalCaloriesBurned

class CalendarView(View):
    def __init__(self):
        self.selectedMonth = datetime.now().year # default to current month
        self.selectedYear = datetime.now().month # default to current year
        
    def get(self, request, *args, **kwargs):        
        response_data = {
            "daysExercisedMonthly": self.daysExercisedMonthly(),
            "hoursExercisedMonthly": self.hoursExercisedMonthly(),
            "distanceCoveredMonthly": self.distanceCoveredMonthly(),
            "datesExercised": self.datesExercised()
        }
        return HttpResponse(json.dumps(response_data))
    
    # Count number of days the user worked out in a month
    def daysExercisedMonthly(self):
        sqlStatement = f'''
            SELECT COUNT(*) 
            FROM metrics_activitylog 
            WHERE EXTRACT(MONTH FROM datetime) = {self.selectedYear} AND EXTRACT(YEAR FROM datetime) = {self.selectedMonth};
        '''
        cursor = connection.cursor()
        cursor.execute(sqlStatement)
        countDaysExercised = cursor.fetchone()[0]
        return countDaysExercised
    
    # Aggregate the hours exercised varying by the month. Keep the default month and year as the current date
    def hoursExercisedMonthly(self):
        sqlStatement = f'''
            SELECT SUM(elapsed_seconds) as total_exercise_time 
            FROM metrics_activitylog 
            WHERE EXTRACT(MONTH FROM datetime) = {self.selectedYear} AND EXTRACT(YEAR FROM datetime) = {self.selectedMonth};
        '''
        cursor = connection.cursor()
        cursor.execute(sqlStatement)
        totalHours = cursor.fetchone()[0]
        return totalHours
    
    # Aggregate the distance covered varying by the month. Keep the default month and year as the current date
    def distanceCoveredMonthly(self):
        sqlStatement = f'''
            SELECT SUM(distance_km) as total_exercise_time 
            FROM metrics_activitylog 
            WHERE EXTRACT(MONTH FROM datetime) = {self.selectedYear} AND EXTRACT(YEAR FROM datetime) = {self.selectedMonth};
        '''
        cursor = connection.cursor()
        cursor.execute(sqlStatement)
        totalDistance = cursor.fetchone()[0]
        return totalDistance
    
    # Get specific days of the month the user worked out
    def datesExercised(self):
        sqlStatement = f'''
            SELECT DISTINCT(TO_CHAR(datetime, 'YYYY-MM-DD')) AS date_only
            FROM metrics_activitylog 
            WHERE EXTRACT(MONTH FROM datetime) = {self.selectedYear} AND EXTRACT(YEAR FROM datetime) = {self.selectedMonth};
        '''
        cursor = connection.cursor()
        cursor.execute(sqlStatement)
        datesExercised = cursor.fetchall()
        lstDatesExercised = [f"{value[0]}" for value in datesExercised]
        return lstDatesExercised
    
class StatsView(View):
    def get(self, request, *args, **kwargs):
        response_data = {
            'distanceStats': self.distanceStats(),
            'timeStats': self.elapsedTimeStats()
        }
        return HttpResponse(json.dumps(response_data))
    
    # Group the month stats for the distance
    def distanceStats(self):
        sqlStatement = f'''
            SELECT 
                CAST(EXTRACT(YEAR FROM datetime) as integer) as year,
                CAST(EXTRACT(MONTH FROM datetime) as integer) as month, 
                SUM(distance_km) AS distanceMonthlySum 
            FROM metrics_activitylog 
            GROUP BY year, month
        '''
        cursor = connection.cursor()
        cursor.execute(sqlStatement)
        totalDistanceStats = cursor.fetchall()
        dictDistanceStats = list(map(lambda x: {'year': x[0], 'month': x[1], 'distance': x[2]}, totalDistanceStats)) # Add labeling and convert to a dict as it was originally in a tuple
        return dictDistanceStats
    
    # Group the month stats for the amount of time exercised
    def elapsedTimeStats(self):
        sqlStatement = f'''
            SELECT 
                CAST(EXTRACT(YEAR FROM datetime) as integer) as year,
                CAST(EXTRACT(MONTH FROM datetime) as integer) as month, 
                SUM(elapsed_seconds) AS distanceMonthlySum 
            FROM metrics_activitylog 
            GROUP BY year, month
        '''
        cursor = connection.cursor()
        cursor.execute(sqlStatement)
        totalTimeStats = cursor.fetchall()
        dictTimeStats = list(map(lambda x: {'year': x[0], 'month': x[1], 'time': x[2]}, totalTimeStats)) # Add labeling and convert to a dict as it was originally in a tuple
        return dictTimeStats 
        
    
    
    
    
    
    
    
