from django.shortcuts import render,redirect
from customer.models import *
from datetime import date,timedelta,datetime
from django.contrib import messages
from customer.forms import ContactForm
# Create your views here.
def homepage(request):
    template="index.html"
    if request.method=='GET':
        cars=Car.objects.filter(status="available")
        return render(request,template,{'cars':cars})

def cars(request):
    template="cars.html"
    if request.method=='GET':
        cars=Car.objects.filter(status="available")
        return render(request,template,{'cars':cars})

def car_detail(request,name):
    template="car-detail.html"
    if request.method=='GET':
        car=Car.objects.get(name=name)
        car_images=CarImage.objects.filter(car=car)
        data={'car':car,
              'car_images':car_images,
              }
        return render(request,template,context=data)

def about_us(request):
    template="about.html"
    if request.method=='GET':
        return render(request,template)

def contact_us(request):
    template="contact.html"
    if request.method=='GET':
        form=ContactForm()
        return render(request,template,{'form':form})
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Thank you! We will get in touch with you soon")
            return redirect("home")
        return render(request,template,{'form':form})
    
def car_booking(request):
    template="car-booking.html"
    if request.method=='GET':
        try:
            id=request.COOKIES.get("cid")
            start_date=request.COOKIES.get("sd")
            end_date=request.COOKIES.get("ed")
            car=Car.objects.get(id=id)
            data={'car':car,
                  'start_date':start_date,
                  'end_date':end_date}
            return render(request,template,context=data)
        except:
            return render(request,"booking-failed.html",{'msg':'Sorry, something went wrong! Please try again'})
    if request.method=='POST':
        try:
            id=request.COOKIES.get("cid")
            car=Car.objects.get(id=id)
            start_date=datetime.strptime(request.COOKIES.get("sd"), "%Y-%m-%d").date()
            next_date=start_date + timedelta(days=1)
            end_date=datetime.strptime(request.COOKIES.get("ed"), "%Y-%m-%d").date()
            if end_date <= start_date:
                return render(request,"booking-failed.html",{'msg':'Sorry, something went wrong! Please try again'})
            if not Reservation.objects.filter(car=car,start_date__gte=start_date,end_date__lte=end_date):
                data=request.POST
                amount=car.price*(end_date-start_date).days
                address=Address.objects.create(h_name=data.get("house"),pin=data.get("pin"),locality=data.get("locality"),
                                    street=data.get("street"),city=data.get("city"),state=data.get("state"),landmark=data.get("landmark"),
                                    country=data.get("country"))
                booking=Booking.objects.create(email=data.get("email"),start_date=start_date,end_date=end_date,amount=amount,name=data.get("name"),phone=data.get("contact"),whatsapp=data.get("whatsapp"),address=address,note=data.get("notes"),id_proof=request.FILES.get("proof"),car=car)
                while start_date < next_date:
                    if start_date==end_date:
                        messages.success(request,"Booking Successful ! You will get an e-mail confirmation soon, thank you!")
                        return redirect("cars")
                    reservation=Reservation.objects.create(car=car,start_date=start_date,end_date=next_date)
                    booking.reservations.add(reservation)
                    start_date += timedelta(days=1)
                    next_date += timedelta(days=1)
                return redirect("car-detail",name=car.name)
            else:
                return render(request,"booking-failed.html",{'msg':'Sorry! Selected vehicle was already booked for the selected dates, please try again with different vehicle!'})
        except:
            return render(request,"booking-failed.html",{'msg':'Sorry, something went wrong! Please try again'})



        
