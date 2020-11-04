from django.contrib import admin
from django.urls import path

from .views import *


urlpatterns = [
    path('', to_menu),
    path('menu/', menu_view),
    path('cassette/all/', cassette_all),
    path('seller/all/', seller_all),
    path('provider/all/', provider_all),
    path('arriving/all/', arriving_all),
    path('selling/all/', selling_all),
    path('seller/add/', seller_create),
    path('cassette/add/', cassette_create),
    path('provider/add/', provider_create),
    path('arriving/add/', arriving_create),
    path('selling/add/', selling_create),
    path('seller/delete/<int:id>', seller_destroy),
    path('cassette/delete/<int:id>', cassette_destroy),
    path('provider/delete/<int:id>', provider_destroy),
    path('arriving/delete/<int:id>', arriving_destroy),
    path('selling/delete/<int:id>', selling_destroy),
    path('seller/edit/<int:id>', seller_edit),
    path('cassette/edit/<int:id>', cassette_edit),
    path('provider/edit/<int:id>', provider_edit),
    path('arriving/edit/<int:id>', arriving_edit),
    path('selling/edit/<int:id>', selling_edit),
    path('seller/update/<int:id>', seller_update),
    path('cassette/update/<int:id>', cassette_update),
    path('provider/update/<int:id>', provider_update),
    path('arriving/update/<int:id>', arriving_update),
    path('selling/update/<int:id>', selling_update),
]
