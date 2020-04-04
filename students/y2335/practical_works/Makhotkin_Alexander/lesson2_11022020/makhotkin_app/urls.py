from django.urls import path

from . import views

urlpatterns = [
    path('owner/<int:owner_id>', views.detail),
    path('list_owners/', views.list_owners),
    path('list_cars/', views.CarsList.as_view()),
    path('owner_form/', views.owner_view),
    path('car_form/', views.CarCreate.as_view()),
]