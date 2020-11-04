from django.contrib import admin
from .models import Farm, Fur, Purchase, Review

# Register your models here.
admin.site.register(Farm)
admin.site.register(Fur)
admin.site.register(Review)
admin.site.register(Purchase)