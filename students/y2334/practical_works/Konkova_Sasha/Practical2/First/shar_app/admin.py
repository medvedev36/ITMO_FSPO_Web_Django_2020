from django.contrib import admin

from .models import Owner, Auto, Drive_docs, Owns

admin.site.register(Owner)
admin.site.register(Auto)
admin.site.register(Drive_docs)
admin.site.register(Owns)