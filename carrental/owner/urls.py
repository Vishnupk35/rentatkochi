from django.urls import path
from owner.views import *

urlpatterns=[
    path("",dashboard,name='dashboard'),
    path("manage-cars",manage_cars,name='manage-cars'),
    path("manage-bookings",manage_bookings,name='manage-bookings'),
    path("manage-enquiries",manage_enquiries,name='manage-enquiries'),
    path("manage-cars/images",manage_car_images,name='manage-car-images'),
    path("manage-cars/features",manage_car_features,name='manage-car-features'),
    path("manage-cars/<int:id>",car_info,name='car-info'),
]