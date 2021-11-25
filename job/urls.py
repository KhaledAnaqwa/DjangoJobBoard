from django.urls import path,include
from . import views

app_name="job"
urlpatterns = [
    path('',views.ListJobs),
    path('<str:slug>',views.JobDetails , name="JobDetails")
]