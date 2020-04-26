from django.urls import path
from . import views
from .views import CarList, CarCreate, list_user

urlpatterns = [
    path('owner/<int:user_id>/', views.owner),
    path('user/', list_user),
    path('car/', CarList.as_view()),
    path('owner_create/', views.create_view),
    path('car_create/', CarCreate.as_view(success_url="/car_create/")),
]
