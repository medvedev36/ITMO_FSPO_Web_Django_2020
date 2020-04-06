from django.contrib import admin

from .models import Person
from .models import Auto
from  .models import Obtaining

admin.site.register(Person)
admin.site.register(Auto)
admin.site.register(Obtaining)
# Register your models here.
