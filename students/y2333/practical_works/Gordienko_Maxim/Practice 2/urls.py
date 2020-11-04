
from django.urls import path
from .views import CarList
from .views import CarCreate
from . import views
from . import forms

urlpatterns = [
     path('user/<int:user_id>/', views.details),
     path('users', views.ListUsers),
     path('UserView/', views.UserView),
     path('cars', CarList.as_view()),
     path('carform/', CarCreate.as_view() )]