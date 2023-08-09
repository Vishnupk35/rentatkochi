from django.shortcuts import redirect
from django.contrib import messages

def login_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_anonymous:
            messages.success(request,"Sorry! You are not logged in")
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_anonymous:
            messages.success(request,"Sorry! You are not logged in")
            return redirect("login")
        
        elif request.user.is_superuser | request.user.is_owner:
            return fn(request,*args,**kwargs)
        else:
            messages.success(request,"Sorry! Access denied")
            return redirect("login")
    return wrapper