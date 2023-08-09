from django.urls import path
from customer.views import *

urlpatterns=[
    path("",homepage,name="home"),
    path("cars",cars,name="cars"),
    path("cars/<str:name>",car_detail,name="car-detail"),
    path("booking",car_booking,name="car-booking"),
    path("contact-us",contact_us,name="contact-us"),
]