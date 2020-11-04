from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('broker_list/all/', BrokerList.as_view(), name='broker-list'),
    path('product_list/all/', ProductList.as_view(), name='product-list'),
    path('provider_list/all/', ProviderList.as_view(), name='provider-list'),
    path('provider_detail/<int:pk>/', ProviderDetail.as_view(), name='provider-detail'),
    path('product_list/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('deal_from/new/', DealForm.as_view(), name='deal-form'),

    path('login/', my_login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('logout/', my_logout, name='logout'),


]