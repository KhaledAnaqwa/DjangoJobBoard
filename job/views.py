from django import forms
from django.db.models.base import Model
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import ApplyForm

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

# def handle_uploaded_file(f):
#     with open("/apply/"+f, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

def JobDetails(request,slug):
    job = Job.objects.get(slug__exact=slug)
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job=job
            myform.save()
            form=ApplyForm()
    else:
        form = ApplyForm()
    context={'job':job,'form':form}
    return render(request,"job/JobDetails.html",context=context)
 