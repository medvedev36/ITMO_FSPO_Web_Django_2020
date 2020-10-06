from django.urls import path

from . import views

urlpatterns = [
    path('owner/<int:Owner_id>/', views.detail),
]