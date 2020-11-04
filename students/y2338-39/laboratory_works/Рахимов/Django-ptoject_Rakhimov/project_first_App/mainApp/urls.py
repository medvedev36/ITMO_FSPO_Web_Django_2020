from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contacts', views.contacts, name='contacts'),
    path('exit', views.exit, name='exit'),
    path('bron', views.bron, name='bron'),
    path('profile', views.profile, name='profile'),
    path('econom', views.EconomListView.as_view(), name='econom'),
    path('standart', views.StandartListView.as_view(), name='standart'),
    path('lux', views.LuxListView.as_view(), name='lux'),
    path('president', views.PresidentListView.as_view(), name='president'),
    path('registration', views.registration, name='registration'),
    path('autorisation', views.autorisation, name='autorisation'),
]
