from django.urls import path,include
from . import views

app_name="job"
urlpatterns = [
    path('',views.ListJobs,name="JobList"),
    path('add',views.AddJob,name="AddJob"),
    path('<str:slug>',views.JobDetails , name="JobDetails")
]