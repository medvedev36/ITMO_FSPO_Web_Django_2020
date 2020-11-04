from django.urls import path

from . import views


urlpatterns = [
    path('', views.CompetitionListView.as_view(), name='competition-list'),
    path('competition/<int:pk>/', views.CompetitionDetailView.as_view(), name='competition-detail'),
    path('competition/new/', views.CompetitionCreateView.as_view(), name='competition-new'),

    path('crew/', views.CrewListView.as_view(), name='crew-list'),
    path('crew/<int:pk>/', views.CrewDetailView.as_view(), name='crew-detail'),

    path('hippodrome/', views.HippodromeListView.as_view(), name='hippodrome-list'),
    path('hippodrome/<int:pk>/', views.HippodromeDetailView.as_view(), name='hippodrome-detail'),

    path('jockey/<int:pk>/', views.JockeyDetailView.as_view(), name='jockey-detail'),

    path('horse/<int:pk>/', views.HorseDetailView.as_view(), name='horse-detail'),

    path('race/new/<int:competition>/', views.enroll_for_competition, name='race-new'),
]
