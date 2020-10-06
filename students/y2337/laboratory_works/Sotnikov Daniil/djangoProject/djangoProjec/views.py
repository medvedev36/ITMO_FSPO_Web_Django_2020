from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic.list import ListView
from django.views.generic.base import View




def ShipView(request):
    ships = Ship.objects.all()
    return render(request, 'shipslist.html', context={'shipslist': ships})


def FuncExcView(request):
    return render(request, 'menuexc.html')


def FuncShipView(request):
    return render(request, 'menuship.html')


def FuncRouteView(request):
    return render(request, 'routemenu.html')


def create_exc(request):
    form = ExcForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "create_exc.html", {'form': form})


def ExcView(request):
    excs = Excursion.objects.all()
    return render(request, 'excursionslist.html', context={'exlist': excs})


def create_ship(request):
    form = ShipForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "create_ship.html", {'form': form})


def create_route(request):
    form = RouteForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "create_route.html", {'form': form})



def edit_route(request, route_id):
    try:
        route = Route.objects.get(route_id=route_id)
        if request.method == "POST":
            route.route_id = request.POST.get("route_id")
            route.name = request.POST.get("name")
            route.days = request.POST.get("days")
            route.stops = request.POST.get("stops")
            route.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "editroute.html", context={"route": route})
    except Route.DoesNotExist:
        return HttpResponseNotFound("<h2>Route not found</h2>")


def delete_ship(request, ship_id):
    try:
        ship = Ship.objects.get(ship_id=ship_id)
        ship.delete()
        return HttpResponseRedirect("/")
    except Ship.DoesNotExist:
        return HttpResponseNotFound("<h2>Ship not found</h2>")


def delete_route(request, route_id):
    try:
        route = Route.objects.get(route_id=route_id)
        route.delete()
        return HttpResponseRedirect("/")
    except Route.DoesNotExist:
        return HttpResponseNotFound("<h2>Route not found</h2>")

def delete_exc(request, excursion_id):
    try:
        exc = Excursion.objects.get(excursion_id=excursion_id)
        exc.delete()
        return HttpResponseRedirect("/")
    except Excursion.DoesNotExist:
        return HttpResponseNotFound("<h2>Excursion not found</h2>")


def edit_exc(request, excursion_id):
    try:
        excursion = Excursion.objects.get(excursion_id=excursion_id)

        if request.method == "POST":
            excursion.excursion_id = request.POST.get("excursion_id")
            excursion.departure = request.POST.get("departure")
            excursion.economy_pass = request.POST.get("economy_pass")
            excursion.business_pass = request.POST.get("business_pass")
            excursion.luxurious_pass = request.POST.get("luxurious_pass")
            excursion.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "editexcursion.html", context={"exc": excursion})

    except Route.DoesNotExist:
        return HttpResponseNotFound("<h2>Excursion not found</h2>")


def edit_ship(request, ship_id):
    try:
        ship = Ship.objects.get(ship_id=ship_id)
        if request.method == "POST":
            ship.ship_id = request.POST.get("ship_id")
            ship.name = request.POST.get("name")
            ship.release = request.POST.get("release")
            ship.deadline = request.POST.get("deadline")
            ship.team = request.POST.get("team")
            ship.economy_price = request.POST.get("economy_price")
            ship.business_price = request.POST.get("business_price")
            ship.luxury_price = request.POST.get("luxury_price")
            ship.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "editship.html", context={"ship": ship})
    except Route.DoesNotExist:
        return HttpResponseNotFound("<h2>Ship not found</h2>")


def MenuView(request):
    return render(request, 'menu.html')


def RouteView(request):
    routes = Route.objects.all()
    return render(request, 'routeslist.html', context={'routeslist': routes})
# # Create your views here.
