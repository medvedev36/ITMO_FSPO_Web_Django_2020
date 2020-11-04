from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic.list import ListView
from django.views.generic.base import View



def MenuView(request):
    return render(request, 'menu.html')

def PatrolView(request):
    patrols = Patrol.objects.all()
    return render(request, 'patrol_list.html', context={'patrollist': patrols})


def BoatView(request):
    boats = Boat.objects.all()
    return render(request, 'boats_list.html', context={'boatlist': boats})

def OfficerView(request):
    officers = Officer.objects.all()
    return render(request, 'officer_list.html', context={'officerlist': officers})


def FuncBoatView(request):
    return render(request, 'menu_boat.html')

def FuncOfficerView(request):
    return render(request, 'menu_officer.html')

def FuncPatrolView(request):
    return render(request, 'menu_patrol.html')


def create_boat(request):
    form = BoatForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "create_boat.html", {'form': form})

def create_officer(request):
    form = OfficerForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "create_officer.html", {'form': form})

def create_patrol(request):
    form = PatrolForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "create_patrol.html", {'form': form})



def edit_patrol(request, patrol_id):
    try:
        patrol = Patrol.objects.get(patrol_id=patrol_id)
        if request.method == "POST":
            patrol.patrol_id = request.POST.get("patrol_id")
            patrol.name = request.POST.get("boat_num")
            patrol.stops = request.POST.get("date")
            patrol.days = request.POST.get("district")
            patrol.stops = request.POST.get("intruders")
            patrol.stops = request.POST.get("reward")
            patrol.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_patrol.html", context={"patrol": patrol})
    except Patrol.DoesNotExist:
        return HttpResponseNotFound("<h2>Patrol not found</h2>")

def edit_boat(request, boat_number):
    try:
        boat = Boat.objects.get(boat_number=boat_number)

        if request.method == "POST":
            boat.boat_number = request.POST.get("boat_number")
            boat.mark = request.POST.get("mark")
            boat.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_boat.html", context={"boat": boat})

    except Boat.DoesNotExist:
        return HttpResponseNotFound("<h2>Boat not found</h2>")


def edit_officer(request, badge):
    try:
        officer = Officer.objects.get(badge=badge)
        if request.method == "POST":
            officer.badge = request.POST.get("badge")
            officer.surname = request.POST.get("surname")
            officer.post = request.POST.get("post")
            officer.enrollment = request.POST.get("enrollment")
            officer.experience = request.POST.get("experience")
            officer.birthday = request.POST.get("birthday")
            officer.boat_number = request.POST.get("boat_number")
            officer.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_officer.html", context={"officer": officer})
    except Officer.DoesNotExist:
        return HttpResponseNotFound("<h2>Officer not found</h2>")

def delete_officer(request, badge):
    try:
        officer = Officer.objects.get(badge = badge)
        officer.delete()
        return HttpResponseRedirect("/")
    except Officer.DoesNotExist:
        return HttpResponseNotFound("<h2>Officer not found</h2>")


def delete_patrol(request, patrol_id):
    try:
        patrol = Patrol.objects.get(patrol_id=patrol_id)
        patrol.delete()
        return HttpResponseRedirect("/")
    except Patrol.DoesNotExist:
        return HttpResponseNotFound("<h2>Patrol not found</h2>")

def delete_boat(request, boat_number):
    try:
        boat = Boat.objects.get(boat_number=boat_number)
        boat.delete()
        return HttpResponseRedirect("/")
    except Boat.DoesNotExist:
        return HttpResponseNotFound("<h2>Boat not found</h2>")







# # Create your views here.
