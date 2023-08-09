from django.shortcuts import render,redirect
from customer.models import *
from owner.forms import CarForm,CarImageForm,CarFeatureForm
from django.contrib import messages
from accounts.decorators import signin_required

# Create your views here.
@signin_required
def dashboard(request):
    template="dashboard.html"
    return render(request,template)

@signin_required
def manage_cars(request):
    template="manage-cars.html"
    cars=Car.objects.all()
    if request.method=='GET':
        form=CarForm()
        return render(request,template,{'cars':cars,'form':form})
    if request.method=='POST':
        form=CarForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Car added successfully!")
            return redirect("manage-cars")
        return render(request,template,{'cars':cars,'form':form})

@signin_required
def manage_car_features(request):
    template="manage-features.html"
    features=CarFeature.objects.all()
    form=CarFeatureForm()
    if request.method=='GET':
        return render(request,template,{'features':features,'form':form})
    if request.method=='POST':
        form=CarFeatureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"New Feature added successfully!")
            return redirect("manage-car-features")
        return render(request,template,{'form':form,'features':features})
    
@signin_required
def manage_bookings(request):
    template="manage-bookings.html"
    bookings=Booking.objects.all()
    if request.method=='GET':
        return render(request,template,{'bookings':bookings})

@signin_required
def manage_enquiries(request):
    template="manage-enquiries.html"
    enquiries=Contact.objects.all()
    if request.method=='GET':
        return render(request,template,{'enquiries':enquiries})

@signin_required
def manage_car_images(request):
    template="manage-car-images.html"
    car_images=CarImage.objects.all()
    if request.method=='GET':
        form=CarImageForm()
        return render(request,template,{'car_images':car_images,'form':form})
    if request.method=='POST':
        form=CarImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"New Image added successfully!")
            return redirect("manage-car-images")
        return render(request,template,{'car_images':car_images,'form':form})

@signin_required
def car_info(request,id):
    template="car-info.html"
    if request.method=='GET':
        car=Car.objects.get(id=id)
        return render(request,template,{'car':car})