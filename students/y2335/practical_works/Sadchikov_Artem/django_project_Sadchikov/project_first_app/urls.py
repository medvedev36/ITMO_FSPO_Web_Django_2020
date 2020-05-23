from django.urls import path
from .views import *
from .views import CarCreate

from .views import ShowCar
urlpatterns = [
    path('owner/<int:car_owner_id>/', owner),
    path('create_owner/', create_owner),
    path('show_owner/', show_owner),
    path('create_car/', CarCreate.as_view()),
    path('show_car/', ShowCar.as_view()),
]
