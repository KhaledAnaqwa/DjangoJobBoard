from django.urls import path,include
from . import views,api

app_name="job"
urlpatterns = [
    path('',views.ListJobs,name="JobList"),
    path('api/list',api.JobListApi,name="JobListApi"),
    path('add',views.AddJob,name="AddJob"),
    path('<str:slug>',views.JobDetails , name="JobDetails")
]