from django.contrib import admin
from .models import ClientUser, License, Rent, CarClass, Car, PickUpPoint

# Register your models here.
admin.site.register(ClientUser)
admin.site.register(Rent)
admin.site.register(CarClass)
admin.site.register(Car)
admin.site.register(License)
admin.site.register(PickUpPoint)

