from django.urls import path, include
from project_first_app.views import *

urlpatterns = [
    path('person/<int:person_id>', detail)
]