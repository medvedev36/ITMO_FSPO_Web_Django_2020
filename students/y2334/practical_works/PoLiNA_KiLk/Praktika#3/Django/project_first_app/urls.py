from django.urls import path

from .views import list_view, CarView

urlpatterns = [
    path('users/', list_view),
    path('cars/', CarView.as_view(template_name="car_list.html"))
]
