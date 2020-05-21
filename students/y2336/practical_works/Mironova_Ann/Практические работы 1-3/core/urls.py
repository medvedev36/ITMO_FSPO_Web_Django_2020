from . import views
from django.urls import path


urlpatterns = [
    path('owner/profile/<int:fk>', views.index, name='profile'),
    path('owner/all/', views.list_owner, name='all-owners'),
    path('owner/new', views.form_owner, name='new-owner'),
    path('vehicle/all', views.VehicleListView.as_view(), name='all-vehicles'),
    path('vehicle/new', views.VehicleCreate.as_view(), name='new-vehicle'),
]
