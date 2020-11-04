from django.urls import path
from . import views
from .views import Cars
from .views import CarView

urlpatterns = [
    path('owner/<int:owner_id>/', views.details),
    path('owners', views.owner_view),
    path('cars', Cars.as_view()),
    path('owner_form', views.owner_form_view),
    path('car_form', CarView.as_view(success_url='car_form')),
]
