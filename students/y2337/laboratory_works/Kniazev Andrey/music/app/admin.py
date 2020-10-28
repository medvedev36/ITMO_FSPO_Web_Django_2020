from django.contrib import admin
from .models import *

admin.site.register(Author)
admin.site.register(Music)
admin.site.register(Disk)
admin.site.register(Producer)