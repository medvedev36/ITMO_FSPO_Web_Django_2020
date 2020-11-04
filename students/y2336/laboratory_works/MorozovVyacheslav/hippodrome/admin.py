from django.contrib import admin
from .models import *

# Register your models here.
models = [Jockey, Horse, Crew, Race, Hippodrome, Competition]
admin.site.register(models)