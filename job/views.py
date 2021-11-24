from django.db.models.base import Model
from django.http.response import HttpResponse
from django.shortcuts import render

import job
from .models import Job,Category
# Create your views here.

def ListJobs(request):
    list = Job.objects.all()
    # return HttpResponse(list)
    context={'jobs':list}
    return render(request,"job/JobList.html",context=context)

def JobDetails(request,id):
    job = Job.objects.get(id__exact=id)
    context={'job':job}
    return render(request,"job/JobDetails.html",context=context)
 