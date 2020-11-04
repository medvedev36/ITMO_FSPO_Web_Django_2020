from django.contrib import admin
from .models import *


models = [Client, Relationship, Attraction, Price, Operation, Platform]
admin.site.register(models)

# Register your models here.
