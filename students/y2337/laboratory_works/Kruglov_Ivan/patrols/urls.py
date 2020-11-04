from .views import *
from django.urls import path

urlpatterns = [
    path('', MenuView, name='Menu'),
    path('boats/', FuncBoatView, name='Boats'),
    path('boats/list/', BoatView),
    path('boats/list/del/<int:boat_number>', delete_boat),
    path('boats/list/edit/<int:boat_number>', edit_boat),
    path('boats/create/', create_boat),
    path('patrols/', FuncPatrolView, name='Patrols'),
    path('patrols/list/', PatrolView),
    path('patrols/list/del/<int:patrol_id>', delete_patrol),
    path('patrols/list/edit/<int:patrol_id>', edit_patrol),
    path('patrols/create/', create_patrol),
    path('officers/', FuncOfficerView, name='Officers'),
    path('officers/list/', OfficerView),
    path('officers/list/del/<int:badge>', delete_officer),
    path('officers/list/edit/<int:badge>', edit_officer),
    path('officers/create/', create_officer),
]
