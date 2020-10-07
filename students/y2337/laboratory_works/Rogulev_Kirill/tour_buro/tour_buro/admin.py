from django.contrib import admin

from tour_buro.models import *

class BusAdmin(admin.ModelAdmin):

    list_display = ("id","name","mileage")


admin.site.register(Bus)
admin.site.register(Excursion_route)
admin.site.register(Crew_member)
admin.site.register(Completed_trip)
