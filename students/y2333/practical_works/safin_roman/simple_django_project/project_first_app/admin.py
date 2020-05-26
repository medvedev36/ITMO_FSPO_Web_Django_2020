from django.contrib import admin
from .models import Car, User, License, Ownership
admin.site.register(User)
admin.site.register(Car)
admin.site.register(License)
admin.site.register(Ownership)
# Register your models here.
