from django.urls import path
from .views import get_jobs, get_single_job, subscribe

urlpatterns = [
    path('jobs/', get_jobs, name="jobs_view"),
    path('jobs/<int:id>/', get_single_job, name="job_view"),
    path('jobs/<int:id>/subscribe', subscribe, name="subscribe"),    
]