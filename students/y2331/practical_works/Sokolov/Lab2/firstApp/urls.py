from django.urls import path
from . import views  # подключение файла контроллеров,описанного в пункте 3

urlpatterns = [
    path('owner/<int:CarOwner_id>/', views.detail),
    path('ex1/',views.list_view),
    path('ex2/', views.GeeksList.as_view()),
    path('ex3/', views.create_view),
    path('ex4/', views.GeeksCreate.as_view()),
]
