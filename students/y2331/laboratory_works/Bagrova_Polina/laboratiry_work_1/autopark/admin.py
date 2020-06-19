from django.contrib import admin
from autopark.models import *


class DriversAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "category", "user")


class CarsAdmin(admin.ModelAdmin):
    list_display = ("license_plate", "model")


class ManifestsAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "driver", "car")


class ClientsAdmin(admin.ModelAdmin):
    list_display = ("name", "address")


class ModelsAdmin(admin.ModelAdmin):
    list_display = ("model", "brand")


class OrdersAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "direction", "second_point")


class ItemsAdmin(admin.ModelAdmin):
    list_display = ("name",)


class OrderCompositionAdmin(admin.ModelAdmin):
    list_display = ("order", "item", "quantity")


admin.site.register(Drivers, DriversAdmin)
admin.site.register(Cars, CarsAdmin)
admin.site.register(Model_of_car, ModelsAdmin)
admin.site.register(Manifests, ManifestsAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Clients, ClientsAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(Order_composition, OrderCompositionAdmin)
