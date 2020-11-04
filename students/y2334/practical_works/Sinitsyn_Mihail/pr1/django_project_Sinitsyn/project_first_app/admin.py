from django.contrib import admin
from project_first_app.models import *

admin.site.site_header = 'm1kshoj'

admin.site.register(Person)
admin.site.register(DriverDoc)
admin.site.register(Ownership)
admin.site.register(Auto)
