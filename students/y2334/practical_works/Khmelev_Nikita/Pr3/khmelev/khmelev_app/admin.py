from django.contrib import admin
from .models import Owner
from .models import Ownership
from .models import Car
from .models import License
from .models import OwnerExt

admin.site.register(Owner)
admin.site.register(Ownership)
admin.site.register(Car)
admin.site.register(License)
admin.site.register(OwnerExt)
# Register your models here.