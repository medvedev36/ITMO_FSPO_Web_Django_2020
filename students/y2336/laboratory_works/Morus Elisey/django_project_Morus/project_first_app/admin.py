from django.contrib import admin
from .models import *


class Admin(admin.ModelAdmin):
    pass


admin.site.register(User)
admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(DriverLicense)
admin.site.register(Ownership)

