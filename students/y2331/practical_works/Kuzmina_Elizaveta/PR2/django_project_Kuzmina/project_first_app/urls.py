from django.urls import path
from . import views
from .views import list_cars,view_cars

urlpatterns = [
    path('date/',views.current_datetime),
    path('owner/<int:CarOwner_id>/', views.detail),
    path('list_owners/', views.list_owners),
    path('list_cars/', list_cars.as_view()),
    path('view_cars/', view_cars.as_view(),name='view_car'),
    path('view_owners/', views.owner_view),
]
