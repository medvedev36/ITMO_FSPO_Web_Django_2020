from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import *
from .forms import *


def owner_detail(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner doesn't exists")
    return render(request, 'owner/detail.html', {'owner': owner})


def owner_list(request):
    return render(request, 'owner/list.html', {'owners': Owner.objects.all()})


def owner_add(request):
    form = AddOwner(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "owner/add.html", {'owner': form})


def car_detail(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)
    except Owner.DoesNotExist:
        raise Http404("Owner doesn't exists")
    return render(request, 'car/detail.html', {'car': car})


class CarList(ListView):
    model = Car
    template_name = 'car/list.html'


class AddCar(CreateView):
    model = Car
    fields = ['brand', 'model', 'color', 'number']
    template_name = 'car/add.html'


# œŒ”ƒŒÀﬂ“‹


# def create_view(request):
#     form = GeeksForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     return render(request, "create_view.html", {'form': form})


class GeeksCreate(CreateView):
    model = GeeksModel
    fields = ['title', 'description']
    template_name = 'create_view.html'
