from django.contrib import admin

from .models import(Owner)
from .models import(Have)
from .models import(Car)

admin.site.register(Owner)
admin.site.register(Have)
admin.site.register(Car)
# Register your models here.
