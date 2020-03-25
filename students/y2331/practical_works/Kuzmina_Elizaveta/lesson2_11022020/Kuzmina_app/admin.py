from django.contrib import admin
from .models import Auto,User,AutoUser,DriverLicence
# Register your models here.
admin.site.register(Auto)
admin.site.register(User)
admin.site.register(AutoUser)
admin.site.register(DriverLicence)

