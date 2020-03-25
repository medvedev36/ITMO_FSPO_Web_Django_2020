from django.contrib import admin
from django.urls import path, include
from Ivakhniuk_app import views
urlpatterns = [

    path('app_date/', views.current_datetime),
    path('detail/<int:poll_id>/', views.detail),
]