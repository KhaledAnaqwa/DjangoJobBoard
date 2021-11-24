from django.db.models.base import Model
from django.http.response import HttpResponse
from django.shortcuts import render

import job
from .models import Job,Category
# Create your views here.

def ListJobs(request):
    return HttpResponse("ListJobs")

def JobDetails(request,id):
    return HttpResponse("JobDetails"+str(id))
 