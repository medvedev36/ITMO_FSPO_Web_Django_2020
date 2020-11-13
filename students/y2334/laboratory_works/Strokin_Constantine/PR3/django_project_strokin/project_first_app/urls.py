from django.urls import path
from project_first_app import views
from project_first_app.views import CarsList, UsersList, CreateCar

urlpatterns = [
    path('owner/<int:id>/', views.Owner_),
    path('owners/', views.Owners_),
    path('cars/', CarsList.as_view()),
    path('users/', UsersList.as_view()),
    path('createowner/', views.CreateOwner),
    path('createcar/', CreateCar.as_view()),
]