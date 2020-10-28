from django.contrib import admin
from project_first_app.models import *

admin.site.site_header = 'Dan4ik'

admin.site.register(User)
admin.site.register(Person)
admin.site.register(DriverDoc)
admin.site.register(Ownership)
admin.site.register(Auto)
