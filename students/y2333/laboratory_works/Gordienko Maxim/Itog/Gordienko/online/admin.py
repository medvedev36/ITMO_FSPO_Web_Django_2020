from django.contrib import admin

from .models import *

# Register your models here.
models = [Customer, Product, Store, Brand, Category, InStock, Purchase]
admin.site.register(models)

