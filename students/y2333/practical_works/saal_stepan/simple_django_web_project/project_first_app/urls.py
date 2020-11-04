from django.urls import path
from .views import CarsList, CarsForm

from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.details),
    path('owners/', views.listOwners),
    path('cars/', CarsList.as_view()),
    path('owner/new', views.owner_form),
    path('car/new', CarsForm.as_view())
]
