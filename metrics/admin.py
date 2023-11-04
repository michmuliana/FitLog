from django.contrib import admin
from .models import User, ActivityLog, Goal

# Register your models here.

admin.site.register(User)
admin.site.register(ActivityLog)
admin.site.register(Goal)

# class ActivityLogAdmin(admin.ModelAdmin):
    
# class GoalsAdmin(admin.ModelAdmin):
    