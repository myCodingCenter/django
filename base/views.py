from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from base.models import Profile


# Create your views here.


@login_required
def home(request):
    user = User
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
            # account info
            username = request.POST.get('username')
            if User.objects.filter(username=username).exists():
                 messages.error(request,'Username already exists')
                 return render(request,'base/register.html')
                # auto generate user to be made 
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')


            if len(password) < 4:
                 messages.error(request,"password too short")
                 return render(request,'base/register.html')
            if password != confirm_password:
                 messages.error(request,"password does not match")
                 return render(request,'base/register.html')
            

            user = User.objects.create_user(username=username,password=password)
            user.save()
            print(user)
            # personal info
            role = request.POST.get('role')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            user.role = role
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            # print(firstname,lastname,username,password,confirm_password,role)
            profile = Profile.objects.create(user=user,role=role)
            profile.save()

            messages.success(request,"Account created successfully")
            return redirect("login_view")

        return render(request,'base/register.html')


def logout_view(request):
     logout(request)
     messages.success(request,"logout successfully")
     return redirect('login_view')