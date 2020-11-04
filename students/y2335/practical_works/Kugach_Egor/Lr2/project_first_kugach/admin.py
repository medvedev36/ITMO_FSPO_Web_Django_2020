from django.contrib import admin

# Register your models here.

from .models import Owner
from .models import Auto
from .models import License
from .models import Owning

admin.site.register(Owner)
admin.site.register(Auto)
admin.site.register(License)
admin.site.register(Owning)