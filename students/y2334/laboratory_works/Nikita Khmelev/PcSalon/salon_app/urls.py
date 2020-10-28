from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('broker_list/all/', BrokerList.as_view(), name='broker-list'),
    path('cd_list/all/', CDList.as_view(), name='cd-list'),
    path('firm_list/all/', FirmList.as_view(), name='firm-list'),
    path('firm_detail/<int:pk>/', FirmDetail.as_view(), name='firm-detail'),
    path('cd_list/<int:pk>/', CDDetail.as_view(), name='cd-detail'),
    path('deal_from/new/', DealForm.as_view(), name='deal-form'),

    path('login/', my_login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('logout/', my_logout, name='logout'),


]