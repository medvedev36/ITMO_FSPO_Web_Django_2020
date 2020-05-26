from django.urls import path
from django.urls import reverse
from . import views
from .views import Cars
from .views import CarCreate

urlpatterns = [
    path('owner/<int:owner_id>/', views.details),
    path('owners', views.owner_view),
    path('car', Cars.as_view()),
    path('owner_form', views.owner_form_view),
    path('car_form', CarCreate.as_view(success_url='car_form')),
]
