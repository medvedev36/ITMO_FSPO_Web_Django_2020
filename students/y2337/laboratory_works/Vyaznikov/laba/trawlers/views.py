from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic.list import ListView
from django.views.generic.base import View



def MenuView(request):
    return render(request, 'menu.html')

def CrewView(request):
    crews = Crew.objects.all()
    return render(request, 'crew_list.html', context={'crewlist': crews})


def VoyageView(request):
    voyages = Voyage.objects.all()
    return render(request, 'voyages_list.html', context={'voyagelist': voyages})

def TrawlerView(request):
    trawlers = Trawler.objects.all()
    return render(request, 'trawler_list.html', context={'trawlerlist': trawlers})


def FuncVoyageView(request):
    return render(request, 'menu_voyage.html')

def FuncTrawlerView(request):
    return render(request, 'menu_trawler.html')

def FuncCrewView(request):
    return render(request, 'menu_crew.html')


def create_voyage(request):
    form = VoyageForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "create_voyage.html", {'form': form})

def create_trawler(request):
    form = TrawlerForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "create_trawler.html", {'form': form})

def create_crew(request):
    form = CrewForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "create_crew.html", {'form': form})



def edit_crew(request, member_id):
    try:
        crew = Crew.objects.get(crew_id=crew_id)
        if request.method == "POST":
            crew.member_id = request.POST.get("member_id")
            crew.trawler_id = request.POST.get("trawler_id")
            crew.member_name = request.POST.get("member_name")
            crew.member_job = request.POST.get("member_job")
            crew.hire_date = request.POST.get("hire_date")
            crew.bday = request.POST.get("bday")
            crew.to_pension = request.POST.get("to_pension")
            crew.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_crew.html", context={"crew": crew})
    except Crew.DoesNotExist:
        return HttpResponseNotFound("<h2>Crew not found</h2>")

def edit_voyage(request, voyage_id):
    try:
        voyage = Voyage.objects.get(voyage_id=voyage_id)

        if request.method == "POST":
            voyage.voyage_id = request.POST.get("voyage_id")
            voyage.trawler_id = request.POST.get("trawler_id")
            voyage.start_date = request.POST.get("start_date")
            voyage.end_date = request.POST.get("end_date")
            voyage.bank_name = request.POST.get("bank_name")
            voyage.fish_name = request.POST.get("fish_name")
            voyage.fish_quantity = request.POST.get("fish_quantity")
            voyage.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_voyage.html", context={"voyage": voyage})

    except Voyage.DoesNotExist:
        return HttpResponseNotFound("<h2>Voyage not found</h2>")


def edit_trawler(request, trawler_id):
    try:
        trawler = Trawler.objects.get(trawler_id=trawler_id)
        if request.method == "POST":
            trawler.trawler_id = request.POST.get("trawler_id")
            trawler.tname = request.POST.get("tname")
            trawler.displacement = request.POST.get("displacement")
            trawler.prod_date = request.POST.get("prod_date")
            trawler.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_trawler.html", context={"trawler": trawler})
    except Trawler.DoesNotExist:
        return HttpResponseNotFound("<h2>Trawler not found</h2>")

def delete_trawler(request, trawler_id):
    try:
        trawler = Trawler.objects.get(trawler_id = trawler_id)
        trawler.delete()
        return HttpResponseRedirect("/")
    except Trawler.DoesNotExist:
        return HttpResponseNotFound("<h2>Trawler not found</h2>")


def delete_crew(request, member_id):
    try:
        crew = Crew.objects.get(member_id=member_id)
        crew.delete()
        return HttpResponseRedirect("/")
    except Crew.DoesNotExist:
        return HttpResponseNotFound("<h2>Crew not found</h2>")

def delete_voyage(request, voyage_id):
    try:
        voyage = Voyage.objects.get(voyage_id=voyage_id)
        voyage.delete()
        return HttpResponseRedirect("/")
    except Voyage.DoesNotExist:
        return HttpResponseNotFound("<h2>Voyage not found</h2>")







# # Create your views here.
