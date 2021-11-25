from django.db.models.base import Model
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

import job
from .models import Job,Category
# Create your views here.

def ListJobs(request):
    list = Job.objects.all()
    paginator = Paginator(list, 1) # Show 5 jobs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # context={'jobs':list,'counts':len(list),'categoreis':Category.objects.all}
    context={'jobs':page_obj,'counts':len(list),'categoreis':Category.objects.all}
    return render(request,"job/JobList.html",context=context)

def JobDetails(request,id):
    job = Job.objects.get(id__exact=id)
    context={'job':job}
    return render(request,"job/JobDetails.html",context=context)
 