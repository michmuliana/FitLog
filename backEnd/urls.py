"""
URL configuration for backEnd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from metrics.views import ActivityLogView, GoalView
#, CalendarView, ActivityLogView, FAQView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('activitylog/', ActivityLogView.as_view(), name='activityLog'),
    path('goal/', GoalView.as_view(), name='goal'),
    # path('', HomeView.as_view(), name='home'),
    # path('calendar/', CalendarView.as_view(), name='calendar'),
    # path('faq/', FAQView.as_view(), name='faq')
    
]
