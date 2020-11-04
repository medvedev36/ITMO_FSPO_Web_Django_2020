from django.contrib import admin
# Register your models here.
from .models import Autoshops, Car_Models, Masters, Costumer, Cars, Comprehensive_Repair, Completed_Works

admin.site.register(Autoshops)
admin.site.register(Car_Models)
admin.site.register(Masters)
admin.site.register(Costumer)
admin.site.register(Cars)
admin.site.register(Comprehensive_Repair)
admin.site.register(Completed_Works)
