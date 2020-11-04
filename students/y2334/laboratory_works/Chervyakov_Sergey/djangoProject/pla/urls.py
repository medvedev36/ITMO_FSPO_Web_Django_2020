from django.urls import path

from .views import *

urlpatterns = [

    path('', attraction_list.as_view(), name='home'),
    path('attraction_list/all/', attraction_list.as_view(), name='attraction_list'),
    path('attraction_detail/<int:pk>/', attraction_detail.as_view(), name='attraction_detail'),
    path('platform_list/all/', platform_list.as_view(), name='platform_list'),
    path('attracion/purchase', deal_form.as_view(), name='deal_form'),


    path('login/', my_login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('logout/', my_logout, name='logout'),

]
