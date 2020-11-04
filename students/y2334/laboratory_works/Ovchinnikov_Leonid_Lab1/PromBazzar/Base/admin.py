from django.contrib import admin
from .models import *
# Register your models here.

models = [Provider, Broker, Product, Supplier, Deals, InDeals, Client]
admin.site.register(models)

