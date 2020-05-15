from django.contrib import admin
from project_first_app.models import Owner
from project_first_app.models import Car
from project_first_app.models import DriverLicense
from project_first_app.models import Ownership
from project_first_app.models import User


class Admin(admin.ModelAdmin):
    pass


admin.site.register(Owner, Admin)
admin.site.register(Car, Admin)
admin.site.register(DriverLicense, Admin)
admin.site.register(Ownership, Admin)
admin.site.register(User, Admin)