from django.contrib import admin

from .models import *

admin.site.register(Owner)
admin.site.register(Auto)
admin.site.register(Certification)
admin.site.register(Possession)
admin.site.register(User)