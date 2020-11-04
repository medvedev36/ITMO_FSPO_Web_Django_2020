from django.contrib import admin
from .models import *
models = [Group, Lesson, Lecture, Teacher, Subject]
admin.site.register(models)

# Register your models here.
