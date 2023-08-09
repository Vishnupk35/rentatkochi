from django.contrib import admin
from customer.models import Car,CarImage,CarFeature,Address,Booking,Reservation,Contact
# Register your models here.
admin.site.register(Car)
admin.site.register(CarImage)
admin.site.register(CarFeature)
admin.site.register(Address)
admin.site.register(Booking)
admin.site.register(Reservation)
admin.site.register(Contact)