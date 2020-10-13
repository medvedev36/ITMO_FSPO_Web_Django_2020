from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from django.views.generic.list import ListView
from .forms import *


class ownerView(ListView):
    model = Owner
    template_name = "2.html"


def carList(request):
    carlist = Car.objects.all()
    return render(request, "1.html", {"carlist": carlist})


def createOwner(request):
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "create.html", {'form': form})


def createCar(request):
    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "create.html", {'form': form})
