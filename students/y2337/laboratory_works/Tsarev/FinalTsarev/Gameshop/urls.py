from django.urls import path, include
from .views import *

urlpatterns = [
    path("", genres_list, name='genre_list_url'),
    path("discs/", discs_list, name='disc_list_url'),
    path('discs_detail/<int:disc_id>/', disc_detail, name='disc_detail_url'),
    path('genre_detail/<int:genre_id>', genre_detail, name='genre_detail_url')
]
