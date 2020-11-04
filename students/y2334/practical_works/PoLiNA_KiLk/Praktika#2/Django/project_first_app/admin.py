from django.contrib import admin
from .models import Person, Car, DriverLicense, Owner

# Register your models here.

admin.site.register(Person)
admin.site.register(Car)
admin.site.register(DriverLicense)
admin.site.register(Owner)
