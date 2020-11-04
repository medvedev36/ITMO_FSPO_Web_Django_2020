from django.urls import path
from adApp.views import *

# URL-адреса для views из файла views.py
urlpatterns = [
    path('shows/', TVShows.as_view()),
    path('advertisings/', Advertisings.as_view()),
    path('adBreaks/', AdBreaks.as_view()),
    path('addshow/', AddTVShows.as_view()),
    path('addadver/', AddAdvertisings.as_view()),
    path('addbreak/', AddAdBreaks.as_view()),
    path('channels/', Channels.as_view()),
    path('advertiser/', Advertisers.as_view()),
    path('advertising/<int:pk>', PutAdvertisings.as_view()),
]
