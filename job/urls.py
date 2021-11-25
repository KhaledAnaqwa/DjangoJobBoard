from django.urls import path,include
from . import views

app_name="job"
urlpatterns = [
    path('',views.ListJobs),
    path('<int:id>',views.JobDetails , name="JobDetails")
]