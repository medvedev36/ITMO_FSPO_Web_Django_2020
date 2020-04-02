from django.contrib import admin
from .models import CarOwner
from .models import Car
from .models import DriversLicense
from .models import Ownership


# Register your models here.

class Admin(admin.ModelAdmin):
    pass


admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(DriversLicense)
admin.site.register(Ownership)
# admin.site.register(CarOwner)
