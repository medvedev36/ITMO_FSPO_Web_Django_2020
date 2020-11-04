from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('owner/<int:owner_id>/', details),
    path('owners', owner_view),
    path('cars', Cars.as_view()),
    path('owner_form', owner_form_view),
    path('car_form', CarCreate.as_view(success_url='car_form')),
]