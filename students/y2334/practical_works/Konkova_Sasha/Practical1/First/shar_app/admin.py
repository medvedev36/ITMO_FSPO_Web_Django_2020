from django.contrib import admin

from .models import Owner
admin.site.register(Owner)

from .models import Auto
admin.site.register(Auto)

from .models import Drive_docs
admin.site.register(Drive_docs)

from .models import Owns
admin.site.register(Owns)