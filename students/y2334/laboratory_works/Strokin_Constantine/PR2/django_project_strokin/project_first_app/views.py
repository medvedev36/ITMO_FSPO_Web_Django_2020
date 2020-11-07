from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Owner, Car
from django.http import HttpResponseNotFound
from .forms import OwnerForm


def Owner_(request, id):
    try:
        owner = Owner.objects.get(id=id)
        return render(request, "Owner.html", {"owner": owner})
    except Owner.DoesNotExist:
        return HttpResponseNotFound("<h2>Owner not found</h2>")


def Owners_(request):
    context = {}
    context["dataset"] = Owner.objects.all()
    return render(request, "Owners.html", context)


class CarsList(ListView):
    model = Car


def CreateOwner(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "CreateOwner.html", context)


class CreateCar(CreateView):
    model = Car
    fields = ['mark', 'model', 'color', 'number']

