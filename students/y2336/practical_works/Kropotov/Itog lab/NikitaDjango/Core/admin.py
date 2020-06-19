from django.contrib import admin
from .models import Client, Fuel, FuelInStation, FuelProvider, FuelStation, Purchase

# Register your models here.
models = [Client, Fuel, FuelInStation, FuelProvider, FuelStation, Purchase]
admin.site.register(models)
