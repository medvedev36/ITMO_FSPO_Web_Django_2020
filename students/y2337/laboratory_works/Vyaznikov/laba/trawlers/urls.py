from .views import *
from django.urls import path

urlpatterns = [
    path('', MenuView, name='Menu'),
    path('voyages/', FuncVoyageView, name='Voyages'),
    path('voyages/list/', VoyageView),
    path('voyages/list/del/<int:voyage_id>', delete_voyage),
    path('voyages/list/edit/<int:voyage_id>', edit_voyage),
    path('voyages/create/', create_voyage),
    path('crews/', FuncCrewView, name='Crews'),
    path('crews/list/', CrewView),
    path('crews/list/del/<int:member_id>', delete_crew),
    path('crews/list/edit/<int:member_id>', edit_crew),
    path('crews/create/', create_crew),
    path('trawlers/', FuncTrawlerView, name='Trawlers'),
    path('trawlers/list/', TrawlerView),
    path('trawlers/list/del/<int:trawler_id>', delete_trawler),
    path('trawlers/list/edit/<int:trawler_id>', edit_trawler),
    path('trawlers/create/', create_trawler),
]
