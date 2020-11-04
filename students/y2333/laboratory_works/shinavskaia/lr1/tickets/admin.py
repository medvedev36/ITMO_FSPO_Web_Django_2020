from django.contrib import admin

from .models import *
from .user import MyUser

# Register your models here.
models = [
    MyUser,
    BusType,
    Station,
    Driver,
    Bus,
    Ride,
    Ticket
]

admin.site.register(models)
