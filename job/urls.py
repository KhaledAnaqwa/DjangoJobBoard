from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.ListJobs),
    path('<int:id>',views.JobDetails)
]