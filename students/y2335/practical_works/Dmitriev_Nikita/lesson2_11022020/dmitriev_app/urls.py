from django.urls import path

from . import views

urlpatterns = [
    path('owner/<int:owner_id>', views.detail),
    path('list_owners/', views.list_owners),
    path('list_cars/', views.CarList.as_view()),
    path('create_owners/', views.create_owners),
    path('create_cars/', views.CarsCreate.as_view()),
]