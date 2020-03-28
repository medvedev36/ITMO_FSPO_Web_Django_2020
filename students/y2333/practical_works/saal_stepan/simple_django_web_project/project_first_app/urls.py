from django.urls import path
from .views import CarsList

from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.details),
    path('owners/', views.listOwners),
    path('cars/', CarsList.as_view())
]
