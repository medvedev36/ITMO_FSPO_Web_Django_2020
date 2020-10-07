from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('auto/<int:auto_id>', detail_auto),
    path('', AutoList.as_view()),
    path('R6S/', AutoCreate.as_view())

]