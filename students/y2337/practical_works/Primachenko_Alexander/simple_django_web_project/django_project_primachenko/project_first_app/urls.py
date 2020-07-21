from django.urls import path
from . import views
from .views import CarList, CarCreate
from .forms import CarForm


urlpatterns = [
    path('owner/<int:owner_id>/', views.owner_dossier),
    path('owner/list/', views.owner_list),
    path('owner/create/', views.owner_create),
    path('car/<int:car_id>/', views.car_dossier),
    path('car/list/', CarList.as_view()),
    path('car/create/', CarCreate.as_view()),
]