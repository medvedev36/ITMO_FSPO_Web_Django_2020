from django.contrib import admin
from .models import User, Car, CarUser, dLicense
admin.site.register(User)
admin.site.register(Car)
admin.site.register(CarUser)
admin.site.register(dLicense)
# Register your models here.