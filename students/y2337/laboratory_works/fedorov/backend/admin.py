from django.contrib import admin
from .models import *

admin.site.register(AppUser)
admin.site.register(Car)
admin.site.register(Repairs)
admin.site.register(Transaction)
admin.site.register(Trip)
admin.site.register(InTripModel)
