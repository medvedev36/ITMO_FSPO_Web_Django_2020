from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('balance/', add_funds, name='add-balance'),
    path('fuelstation/<int:station>/buy/<int:fuel>', buy_fuel, name='purchase-new'),
    path('user/<int:pk>/delete/', ClientDeleteView.as_view(), name='user-delete'),
    path('purchase/<int:pk>/', ClientPurchaseList.as_view(), name='user-purchase'),
    path('fuelstation/all/', FuelStationListView.as_view(), name='fuelstation-list'),
    path('fuelstation/<int:pk>/', FuelStationDetailView.as_view(), name='fuelstation-detail'),
    path('fuelstation/<int:station>/add_fuel/', add_fuel_to_station, name='fuelinstation-new'),
    path('fuelstation/new/', FuelStationCreateView.as_view(), name='fuelstation-new'),
    path('fuelprovider/all/', FuelProviderListView.as_view(), name='fuelprovider-list'),
    path('fuelprovider/<int:pk>/', FuelProviderDetailView.as_view(), name='fuelprovider-detail'),
    path('fuel/<int:pk>/', FuelDetailView.as_view(), name='fuel-detail'),
]