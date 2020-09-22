from django.contrib import admin

from .models import Auto, Owner, Owning, DriveLic, userOwner

admin.site.register(Auto)
admin.site.register(Owner)
admin.site.register(Owning)
admin.site.register(DriveLic)
admin.site.register(userOwner)
