"""lesson_11022020 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Levashova_app import views
from .views import cars_list
from .views import CarCreate

urlpatterns = [
    path('date_app/', views.current_datetime),
    path('user/<int:passport_ID>', views.user),
    path('users', views.list_view),
    path('cars', cars_list.as_view()),
    path('user_form', views.create_view),
    path('car_form', CarCreate.as_view())
]
