
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.current_datetime),
    path('users/<int:passport_num>/', views.detail),
]
