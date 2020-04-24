from django.contrib import admin

from .models import(Car_owner)
from .models import(Possession)
from .models import(Car)

admin.site.register(Car)
admin.site.register(Car_owner)
admin.site.register(Possession)
