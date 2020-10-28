from django.contrib import admin
from .models import *

models = [Client]
admin.site.register(models)


class CDAdmin(admin.ModelAdmin):
    list_display = ('name_cd', 'prod_date', 'descr')


admin.site.register(CD, CDAdmin)


class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'author', 'cd_name')


admin.site.register(Game, GameAdmin)


class BrokerAdmin(admin.ModelAdmin):
    list_display = ('name_brok', 'birthday', 'phone_brok', 'address_brok')


admin.site.register(Broker, BrokerAdmin)


class FirmAdmin(admin.ModelAdmin):
    list_display = ('name_sup', 'address_sup', 'sup_about')


admin.site.register(Firm, FirmAdmin)


class DealAdmin(admin.ModelAdmin):
    list_display = ('code_deal', 'date_deal', 'quantity_sale', 'br_name', 'cd_name')


admin.site.register(Deal, DealAdmin)


class InDealsAdmin(admin.ModelAdmin):
    list_display = ('date_deal', 'deals')


admin.site.register(InDeals, InDealsAdmin)


class SupplyAdmin(admin.ModelAdmin):
    list_display = ('code_supp', 'price', 'date_supp', 'quantity_ad', 'sup_name', 'cd_name')


admin.site.register(Supply, SupplyAdmin)