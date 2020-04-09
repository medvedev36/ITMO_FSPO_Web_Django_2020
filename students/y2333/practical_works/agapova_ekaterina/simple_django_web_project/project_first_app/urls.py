from django.urls import path
from . import views
from .views import CarList, CarsForm


urlpatterns = [
    path('owner/<int:id>/', views.details),
    path('ownerlist', views.owner_list),
    path('carlist', CarList.as_view()),
    path('ownerform', views.owner_form),
    path('carform', CarsForm.as_view())
]
