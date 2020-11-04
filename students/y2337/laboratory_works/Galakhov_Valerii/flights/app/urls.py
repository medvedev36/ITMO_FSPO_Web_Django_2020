from django.urls import path
from .views import *

urlpatterns = [
    path('addFlight/', addFlight, name="add_flight-url"),
    path('addPilot/', addPilot, name="add_pilot-url"),
    path('addHelicopter/', addHelicopter, name="add_helicopter-url"),
    path('', flight_list, name="flight_list-url"),
    path('editCost/<int:id>/', editCost),
    path('delete/<int:id>/', delete),
    path('editDate/<int:id>', editDate),
    path('editHelicopter/<int:id>', editHelicopter),
    path('editDuration/<int:id>', editDuration),
    path('editWeight/<int:id>', editWeight),
]
