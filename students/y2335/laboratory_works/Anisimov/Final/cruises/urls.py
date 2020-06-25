# coding=utf-8
from  django.urls import path
from . import views

urlpatterns = [
    path('', views.tour_list, name = "tour_list"),
    path('thanks/', views.thanks, name = "thanks"),
    path('motorship_list/', views.motorship_list, name = "motorships"),
    path('sailor_list/', views.sailor_list, name = "sailors"),
    path("buy/<int:pk>", views.tour_buy, name = "tour_buy")
]