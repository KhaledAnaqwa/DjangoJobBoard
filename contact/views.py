from django.http import HttpResponse
from django.shortcuts import render
from .models import Info
# Create your views here.

def contact(request):
    info = Info.objects.get()
    return render(request,'contact/contact.html',{"info":info})