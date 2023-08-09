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