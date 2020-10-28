from django.contrib import admin
from .models import Routes, Buses, Staff, Ways, Cities

admin.site.register(Routes)
admin.site.register(Buses)
admin.site.register(Staff)
admin.site.register(Ways)
admin.site.register(Cities)