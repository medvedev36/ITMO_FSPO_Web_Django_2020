from django.urls import path
from . import views
from .views import listOwners, listCars, viewCars,viewOwners
urlpatterns = [
    path('owner/<int:poll_id>', views.detail),
    path('ListOwners', listOwners.as_view(), name='owner-list'),
    path('ListCars', listCars.as_view(), name='cars-list'),
    path('ViewCars', viewCars.as_view(), name='car-view'),
    path('ViewOwners', viewOwners.as_view(), name='owner-view'),
]