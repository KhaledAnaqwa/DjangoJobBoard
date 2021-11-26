
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Profile as userProfile
from .forms import SignUpForm,UserForm,ProfileForm
# Create your views here.

def SignUp(request):
    if request.method =='POST':
        form= SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user= authenticate(username=username,password=password)
            login(request=request,user=user)
            # return redirect("account/")
    else:
        form= SignUpForm()
    
    return render(request,'registration/signup.html',{'form':form})
    # return HttpResponseNotFound("Page not foooooood")
    # return JsonResponse({'Name':'Khaled'})


def Profile(request):
    profile= userProfile.objects.get(user=request.user)
    return render(request,"accounts/profile.html",{'profile':profile})

def EditPorfile(request):
    user=request.user
    profile= userProfile.objects.get(user=user)
    if request.method =='POST':
        userform= UserForm(request.POST, instance=user)
        profileform= ProfileForm(request.POST, request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid() :
            userform.save()
            profileform.save()
            return redirect(reverse("accounts:profile"))
    else:
        userform= UserForm( instance=user)
        profileform= ProfileForm(instance=profile)

    return render(request,"accounts/edit_profile.html",{'user':request.user,'userform':userform,'profileform':profileform})


