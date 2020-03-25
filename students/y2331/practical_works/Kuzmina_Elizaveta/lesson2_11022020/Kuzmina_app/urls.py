from django.urls import path, include
from Kuzmina_app import views

urlpatterns = [
    path('date/',views.current_datetime),
    path('user/<int:pass_num>/', views.detail)
]