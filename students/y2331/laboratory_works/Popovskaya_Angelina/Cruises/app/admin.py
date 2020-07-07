from django.contrib import admin
from .models import *
models = [Profile, Cruise, Excursion, Sell]
admin.site.register(models)
# Register your models here.
