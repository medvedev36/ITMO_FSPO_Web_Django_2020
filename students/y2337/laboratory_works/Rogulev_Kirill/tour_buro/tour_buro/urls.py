
from django.contrib import admin
from django.urls import path, include

from tour_buro.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buses/', bus_view.as_view()),
    path('excursion_routes/',excursion_route_view.as_view()),
    path('crew_members/',crew_member_view.as_view()),
    path('completed_trips/',completed_trip_view.as_view()),
    path('', include('core.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]