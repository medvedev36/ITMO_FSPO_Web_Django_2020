from django.urls import path
from .views import *

urlpatterns = [
    path('owner/<int:car_owner_id>/', owner)
]