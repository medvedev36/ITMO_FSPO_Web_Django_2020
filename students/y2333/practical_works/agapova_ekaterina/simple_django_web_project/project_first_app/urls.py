from django.urls import path
from . import views
from .views import CarList


urlpatterns = [
    path('owner/<int:id>/', views.details),
    path('ownerlist', views.owner_list),
    path('carlist', CarList.as_view())
]
