from django.urls import path
from .views import *

urlpatterns = [
  path('attraction/<int:attraction_id>', Attractions.as_view()),
  path('useattractions', UseAttractions.as_view()),
  path('playgrounds', Playgrounds.as_view()),
  path('types', Types.as_view()),
  path('popular_attraction', PopularAttraction.as_view()),
  path('purchase', Purchase.as_view()),
  path('buyticket/<int:attraction_id>', BuyTicket.as_view()),
]