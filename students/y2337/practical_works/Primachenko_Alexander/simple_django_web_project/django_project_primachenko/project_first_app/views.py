from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404

from .models import Owner, Car
from .forms import OwnerForm, CarForm


def owner_dossier(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    return render(request, 'owner/dossier.html', {'owner': owner})


def owner_list(request):
    return render(request, 'owner/list.html', {'owners_list': Owner.objects.all()})


def owner_create(request):
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'owner/create.html', {'form': form})


def car_dossier(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'car/dossier.html', {'car': car})


class CarList(ListView):
    model = Car
    template_name = 'car/list.html'


class CarCreate(CreateView):
    model = Car
    fields = [
        "manufacturer",
        "model",
        "color",
        "number",
    ]
    template_name = 'car/create.html'
