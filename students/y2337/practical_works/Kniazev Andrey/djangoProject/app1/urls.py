from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('cars/', carList),
    path('owners/', ownerView.as_view()),
    path('addOwner/', createOwner),
    path('addCar/', createCar)
]
