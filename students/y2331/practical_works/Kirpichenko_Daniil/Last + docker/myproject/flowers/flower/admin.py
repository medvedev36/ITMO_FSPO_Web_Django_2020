from django.contrib import admin
from .models import Products,OrderInformation,Orders
# Register your models here.


class Admin(admin.ModelAdmin):
    pass


admin.site.register(Products, Admin)
admin.site.register(OrderInformation, Admin)
admin.site.register(Orders, Admin)
