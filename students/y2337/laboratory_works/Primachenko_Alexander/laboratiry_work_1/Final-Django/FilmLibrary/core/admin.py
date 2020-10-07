from django.contrib import admin
from .models import *

# Register your models here.
myModels = [
    Cassette,
    Seller,
    Provider,
    CassetteArriving,
    CassetteSelling,
]
admin.site.register(myModels)
