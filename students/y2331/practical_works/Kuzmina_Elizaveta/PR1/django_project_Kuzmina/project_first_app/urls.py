from django.urls import path
from . import views

urlpatterns = [
    path('date/',views.current_datetime),
    path('owner/<int:CarOwner_id>/', views.detail),
]
