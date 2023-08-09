from django.db import models
from accounts.models import User

class CarFeature(models.Model):
    name=models.CharField(max_length=100,null=True)
    status=models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=250,null=True)
    brand=models.CharField(max_length=100,null=True)
    price=models.PositiveIntegerField(null=True)
    description=models.TextField(null=True)
    capacity=models.PositiveIntegerField(null=True)
    color=models.CharField(max_length=100,null=True)
    trans_options=(('manual','manual'),
                   ('automatic','automatic'))
    transmission=models.CharField(max_length=25,null=True,choices=trans_options)
    options=(('available','available'),
             ('un-available','un-available'),
             ('on-service','on-service'),)
    status=models.CharField(max_length=25,choices=options,default="available")
    mileage=models.PositiveIntegerField(null=True)
    fuel=models.CharField(max_length=30,null=True)
    image=models.ImageField(null=True,upload_to="images/cars/")
    features=models.ManyToManyField(CarFeature)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    
class CarImage(models.Model):
    car=models.ForeignKey(Car,null=True,on_delete=models.CASCADE)
    image=models.ImageField(null=True,upload_to="images/cars/")
    created=models.DateField(auto_now_add=True)
    status=models.BooleanField(default=True)

class Reservation(models.Model):
    car=models.ForeignKey(Car,null=True,on_delete=models.CASCADE)
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    options=(("booked","booked"),
             ("confirmed","confirmed"),
             ("cancelled","cancelled"),
             ("completed","completed"),
             )
    status=models.CharField(choices=options,max_length=20,default="booked")
    # user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)

class Address(models.Model):
    h_name=models.CharField(max_length=100,null=True)
    pin=models.PositiveIntegerField(null=True)
    locality=models.CharField(max_length=100,null=True)
    street=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    landmark=models.CharField(max_length=100,null=True,blank=True)
    country=models.CharField(max_length=100,null=True)

class Booking(models.Model):
    reservations=models.ManyToManyField(Reservation)
    car=models.ForeignKey(Car,null=True,on_delete=models.CASCADE)
    email=models.CharField(max_length=200,null=True)
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    amount=models.PositiveIntegerField(null=True)
    name=models.CharField(max_length=250,null=True)
    phone=models.CharField(max_length=20,null=True)
    whatsapp=models.CharField(max_length=20,null=True)
    address=models.ForeignKey(Address,null=True,on_delete=models.CASCADE)
    note=models.TextField(null=True)
    created=models.DateTimeField(auto_now_add=True,null=True)
    id_proof=models.FileField(null=True,upload_to="files/id_proofs/")
    options=(("booked","booked"),
             ("confirmed","confirmed"),
             ("in-progress","in-progress"),
             ("cancelled","cancelled"),
             ("completed","completed"),
             )
    status=models.CharField(choices=options,max_length=15,default="booked")

    def __str__(self):
        return self.name

class Contact(models.Model):
    name=models.CharField(max_length=250,null=True)
    email=models.EmailField(null=True)
    subject=models.CharField(max_length=250,null=True)
    message=models.TextField(null=True)
    options=(("new","new"),
             ("pending","pending"),
             ("responded","responded"),
             ("completed","completed"),
             )
    status=models.CharField(choices=options,max_length=15,default="new")
