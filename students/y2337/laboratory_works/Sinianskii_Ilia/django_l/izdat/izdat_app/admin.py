from django.contrib import admin
from .models import *


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Edition)
admin.site.register(Customer)
admin.site.register(Order)

# Register your models here.
