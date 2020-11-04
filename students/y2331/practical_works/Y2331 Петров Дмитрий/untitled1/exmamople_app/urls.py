
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import AvtomList, Avtocreate


urlpatterns = [
    path('', views.current_datetime),
    path('users/<int:passport_num>/', views.detail),
    path('all/', views.list_v),
    path('avt/', AvtomList.as_view()),
    path('adusr/', views.create_view),
    path('addavt/', Avtocreate.as_view()),
]
