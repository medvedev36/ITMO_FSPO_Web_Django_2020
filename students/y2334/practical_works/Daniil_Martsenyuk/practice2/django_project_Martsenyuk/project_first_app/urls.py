from django.urls import path, include
from project_first_app.views import *

urlpatterns = [
    path('person/<int:person_id>', detail),
    path('owners', all_owners),
    path('cars', Cars.as_view()),
    path('car_form', AutosCreate.as_view()),
    path('owner_form', create_owner)
]