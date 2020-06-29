from django.urls import path
from .views import *

urlpatterns = [
    path('car/<int:pk>', CarView.as_view()),
    path('trip/start/', BeginTrip.as_view()),
    path('trip/finish/', EndTrip.as_view()),
    path('history/', History.as_view()),
]