from django.urls import path, include
from belov import views

urlpatterns = [
    path('<int:car_id>', views.detail)
]