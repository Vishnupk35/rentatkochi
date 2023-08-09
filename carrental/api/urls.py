from django.urls import path
from api.views import *
urlpatterns=[
    path("v1/check/availability/",ReservationCheckView.as_view(),name="api-availability-check")
]