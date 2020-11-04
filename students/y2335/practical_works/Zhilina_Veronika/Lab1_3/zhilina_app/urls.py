from . import views

from django.urls import path

urlpatterns = [
    path('owners/<int:owner_id>/', views.detail),
    path('owners/', views.allOwners),
    path('autos/', views.AutoList.as_view()),
    path('createOwner/', views.createOwner),
    path('createAuto/', views.AutoCreate.as_view()),
]