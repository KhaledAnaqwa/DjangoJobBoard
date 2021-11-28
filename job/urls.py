from django.urls import path,include
from . import views,api

user_list = api.JobViewSet.as_view({'get': 'list'})
user_detail = api.JobViewSet.as_view({'get': 'retrieve'})

app_name="job"
urlpatterns = [
    path('',views.ListJobs,name="JobList"),
    #api using functions 
    
    path('api/list',api.JobListApi,name="JobListApi"),
    path('api/jobdetail/<int:id>',api.JobDetailApi,name="JobDetailApi"),
    
    #api using geniraic view
    path('api/v2/list/<int:id>',api.JobListApiV2.as_view(),name="JobListApiV2"),
    
    # api using viewset
    path('api/v3/job/<int:pk>',user_detail,name="JobDetailApiV3"),
    path('api/v3/list/',user_list,name="JobListApiV3"),
    
    path('add',views.AddJob,name="AddJob"),
    path('<str:slug>',views.JobDetails , name="JobDetails")
]