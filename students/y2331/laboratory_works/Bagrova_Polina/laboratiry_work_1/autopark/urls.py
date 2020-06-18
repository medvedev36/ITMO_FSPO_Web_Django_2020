from django.urls import path
from autopark.views import *

urlpatterns = [
    path('drivers/', DriversView.as_view()),
    path('cars/', CarsView.as_view()),
    path('clients/', ClientsView.as_view()),
    path('clients/<int:pk>', ClientsView.as_view()),
    path('manifests/', ManifestsView.as_view()),
    path('manifests/<int:pk>', ManifestsView.as_view()),
    path('orders/', OrdersView.as_view()),
    path('orders/<int:pk>', OrdersView.as_view()),
]
