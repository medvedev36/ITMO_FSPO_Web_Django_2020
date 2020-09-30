from django.urls import path

from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.details),
    path('list_owners/', views.list_owner),
    path('list_cars/', views.CarList.as_view()),
    path('create_owner/', views.create_owner),
    path('create_car/', views.CarCreate.as_view()),
 ]
