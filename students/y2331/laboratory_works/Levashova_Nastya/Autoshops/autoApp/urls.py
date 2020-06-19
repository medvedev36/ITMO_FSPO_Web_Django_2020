from django.urls import path
from autoApp.views import *

urlpatterns = [
    path('shops/', Autoshop.as_view()),
    path('masters/', Master.as_view()),
    path('custumers/', Custumers.as_view()),
    path('cars/', Car.as_view()),
    path('works/', Works.as_view()),
    path('comworks/', ComWorks.as_view()),
    path('work/<int:pk>', Works.as_view()),
    path('models/', Model.as_view()),
]
