from django.urls import path
from .views import CarList
from .views import CarCreate

from . import views
from . import forms

urlpatterns = [
     path('owner/<int:owner_id>/', views.details),
     path('owners/', views.listOwners),
     path('ownerview/', views.ownerView),
     path('cars/', CarList.as_view()),
     path('carform/', CarCreate.as_view() ),
 ]