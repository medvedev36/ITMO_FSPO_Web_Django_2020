from django.contrib import admin
from .models import Owner, License, Car, Possession

admin.site.register(Owner)
admin.site.register(License)
admin.site.register(Car)
admin.site.register(Possession)
