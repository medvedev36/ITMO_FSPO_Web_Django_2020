from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('routes_add/', views.routesformview, name="routes_add"),
    path('buses_add/', views.busesformview, name="buses_add"),
    path('staff_add/', views.staffformview, name="staff_add"),
    path('ways_add/', views.waysformview, name="ways_add"),
    path('cities_add/', views.citiesformview, name="cities_add"),

    path('buses_info/<int:Number>', views.get_buses_info),
    path('staff_info/', views.get_staff_info, name="staff_info")
]