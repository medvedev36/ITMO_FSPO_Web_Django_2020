from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.views import View
from .models import *
from .forms import *


def flight_list(request):
    flights = Flight.objects.all()
    return render(request, "flight_list.html", context={"flight_list": flights})


def addFlight(request):
    form = FlightForm(request.POST or None)
    if form.is_valid():
        new_order = form.save()
        new_order.idHelicopter = form.cleaned_data['idHelicopter']
        new_order.dateOfFlight = form.cleaned_data['dateOfFlight']
        new_order.cargoWeight = form.cleaned_data['cargoWeight']
        new_order.flightDuration = form.cleaned_data['flightDuration']
        new_order.flightCost = form.cleaned_data['flightCost']
        new_order.save()
        return HttpResponseRedirect('/')
    return render(request, "Add.html", {'form': form})


def addPilot(request):
    form = PilotForm(request.POST or None)
    if form.is_valid():
        new_order = form.save()
        new_order.idHelicopter = form.cleaned_data['idHelicopter']
        new_order.pilotName = form.cleaned_data['pilotName']
        new_order.pilotPost = form.cleaned_data['pilotPost']
        new_order.pilotExperience = form.cleaned_data['pilotExperience']
        new_order.dateOfBirth = form.cleaned_data['dateOfBirth']
        new_order.save()
    return render(request, "Add.html", {'form': form})


def addHelicopter(request):
    form = HelicopterForm(request.POST or None)
    if form.is_valid():
        new_order = form.save()
        new_order.name = form.cleaned_data['name']
        new_order.carryingCapacity = form.cleaned_data['carryingCapacity']
        new_order.dateOfProduction = form.cleaned_data['dateOfProduction']
        new_order.save()
    return render(request, "Add.html", {'form': form})


def editCost(request, id):
    flight = Flight.objects.get(id=id)
    if request.method == "POST":
        flight.flightCost = request.POST.get("flightCost")
        flight.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "editCost.html", {"flight": flight})


def editDate(request, id):
    flight = Flight.objects.get(id=id)
    if request.method == "POST":
        flight.dateOfFlight = request.POST.get("dateOfFlight")
        flight.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "editDate.html", {"flight": flight})


def editWeight(request, id):
    flight = Flight.objects.get(id=id)
    if request.method == "POST":
        flight.cargoWeight = request.POST.get("cargoWeight")
        flight.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "editWeight.html", {"flight": flight})


def editDuration(request, id):
    flight = Flight.objects.get(id=id)
    if request.method == "POST":
        flight.flightDuration = request.POST.get("flightDuration")
        flight.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "editDuration.html", {"flight": flight})


def editHelicopter(request, id):
    helicopter = Helicopter.objects.get(id=id)
    if request.method == "POST":
        helicopter.name = request.POST.get("name")
        helicopter.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "editHelicopter.html", {"helicopter": helicopter})


def delete(request, id):
    try:
        flight = Flight.objects.get(id=id)
        flight.delete()
        return HttpResponseRedirect('/')
    except Flight.DoesNotExist:
        return HttpResponseNotFound("<h1>Flight not found</h1>")

