from django.contrib import admin

# Register your models here.
from .models import People
from .models import User
from .models import Car
from .models import License
from .models import Ownership

admin.site.register(People)
admin.site.register(User)
admin.site.register(Car)
admin.site.register(License)
admin.site.register(Ownership)