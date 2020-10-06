from .views import *
from django.urls import path, include
from . import views

urlpatterns = [
    path('ships/list/', ShipView),
    path('ships/list/del/<int:ship_id>', delete_ship),
    path('ships/create/', create_ship),
    path('ships/', FuncShipView, name='Ships'),
    path('route/', FuncRouteView, name='Routes'),
    path('route/list/del/<int:route_id>', delete_route),
    path('route/list/', RouteView),
    path('route/create/', create_route),
    path('', MenuView, name='Menu'),
    path('route/list/editroute/<int:route_id>', views.edit_route),
    path('ships/list/editship/<int:ship_id>', views.edit_ship),
    path('excursions/', FuncExcView, name='Excursions'),
    path('excursions/create/', create_exc),
    path('excursions/list/', ExcView),
    path('excursions/list/editexc/<int:excursion_id>', views.edit_exc),
    path('excursions/list/del/<int:excursion_id>', delete_exc),
]
