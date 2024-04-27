from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.


@login_required
def home(request):
    user = User.objects.all()
    print(user)
    return render(request,'base/home.html',{'user':user})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"Invalid Cedentials! Please try again with correct credentials")
            return render(request,'base/login.html')
    return render(request,'base/login.html')


def register_view(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm-password')

            print(username,password)
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                messages.error(request,"Invalid Cedentials! Please try again with correct credentials")
                return render(request,'base/login.html')
    return render(request,'base/login.html')
    
    return render(request,'base/register.html')