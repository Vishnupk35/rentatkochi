from django.shortcuts import render,redirect
from customer.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from accounts.decorators import login_required

# Create your views here.
#Accounts Management
def register(request):
    template="register.html"
    if request.method=='GET':
        return render(request,template)
    if request.method=='POST':
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        if(password1 != password2):
            messages.success(request,"Passwords not matching")
            return redirect("register")
        if User.objects.filter(email=email).exists():
            messages.success(request,"Sorry! User account already exists with the given email")
            return redirect("register")
        user=User.objects.create_user(email=email,password=password1)
        if user:
            messages.success(request,"User account created successfully! Please log-in now")
            return redirect("login")
        return render(request,template)
    
def log_in(request):
    template="login.html"
    if request.method=='GET':
        if request.user.is_authenticated:
            return redirect("home")
        return render(request,template)
    if request.method=='POST':
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(username=email,password=password)
        if user:
            login(request,user)
            if(request.user.is_superuser | request.user.is_owner):
                return redirect("dashboard")
            else:
                msg=f"Hello  {request.user}  !!!, Welcome to Rent@Kochi !"
                messages.success(request,msg)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect("home")
        else:
            if User.objects.filter(email=email).exists():
                msg="Incorrect password"
            else:
                msg="Incorrect login credentials"
            messages.success(request,msg)
            return redirect("login")

@login_required
def log_out(request):
    logout(request)
    messages.success(request,"Successfully logged out!!!")
    return redirect('login')