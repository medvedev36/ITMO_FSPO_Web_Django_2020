from django.contrib import admin
from .models import(Owner)
from .models import(Ownership)
from .models import(Car)

admin.site.register(Owner)
admin.site.register(Ownership)
admin.site.register(Car)
# Register your models here.
