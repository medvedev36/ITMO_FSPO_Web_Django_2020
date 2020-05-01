from django.contrib import admin
from .models import driver_license, User, Car, Car_User

admin.site.register(driver_license)
admin.site.register(User)
admin.site.register(Car)
admin.site.register(Car_User)

# Register your models here.
