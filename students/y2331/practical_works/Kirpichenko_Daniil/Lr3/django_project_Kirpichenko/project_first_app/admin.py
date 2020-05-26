from django.contrib import admin

# Register your models here.

from .models import Car, Owner, Ownership, DriverLicense, User1

class Admin(admin.ModelAdmin):
    pass


admin.site.register(Owner, Admin)
admin.site.register(Car, Admin)
admin.site.register(DriverLicense, Admin)
admin.site.register(Ownership, Admin)
admin.site.register(User1)
