from django.shortcuts import render, redirect
from django.http import Http404
from .models import Routes, Buses, Staff, Ways, Cities
from .forms import RoutesForm, BusesForm, StaffForm, WaysForm, CitiesForm


def menu(request):
    if request.method=='GET':
        if request.GET.get('staff'):
            return redirect('staff_add')
        if request.GET.get('ways'):
            return redirect('ways_add')
        if request.GET.get('routes'):
            return redirect('routes_add')
        if request.GET.get('buses'):
            return redirect('buses_add')
        if request.GET.get('cities'):
            return redirect('cities_add')

    context = {}
    return render(request, "menu.html", context)


def routesformview(request):
    if request.GET.get('submit'):
        form = RoutesForm(request.GET or None)
        if form.is_valid():
            form.save()
        return redirect("menu")
    context = {}

    form = RoutesForm(request.POST or None)

    context['form'] = form
    return render(request, "routes_add.html", context)


def busesformview(request):
    if request.GET.get('submit'):
        form = BusesForm(request.GET or None)
        if form.is_valid():
            form.save()
        return redirect("menu")
    context ={}

    form = BusesForm(request.POST or None)

    context['form'] = form
    return render(request, "buses_add.html", context)


def staffformview(request):
    if request.POST.get('submit'):
        form = StaffForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect("menu")
    context ={}

    form = StaffForm(request.GET or None)

    context['form'] = form
    return render(request, "staff_add.html", context)


def waysformview(request):
    if request.GET.get('submit'):
        form = WaysForm(request.GET or None)
        if form.is_valid():
            form.save()
        return redirect("menu")
    context ={}

    form = WaysForm(request.POST or None)

    context['form'] = form
    return render(request, "ways_add.html", context)


def citiesformview(request):
    if request.GET.get('submit'):
        form = CitiesForm(request.GET or None)
        if form.is_valid():
            form.save()
        return redirect("menu")
    context ={}

    form = CitiesForm(request.POST or None)

    context['form'] = form
    return render(request, "cities_add.html", context)


def get_staff_info(request):
    try:
        staff = Staff.objects.all()
    except Staff.DoesNotExist:
        raise Http404("No members")
    return render(request, "staff_info.html", {"staff": staff})


def get_buses_info(request, Number):
    try:
        buses = Buses.objects.get(pk=Number)
    except Buses.DoesNotExist:
        raise Http404("No transport")
    return render(request, "buses_info.html", {"bus": buses})
