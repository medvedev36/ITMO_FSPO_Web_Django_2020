from django.contrib import admin
from .models import Owner
from .models import Have_car
from .models import Car

admin.site.register(Owner)
admin.site.register(Have_car)
admin.site.register(Car)

# Register your models here.
