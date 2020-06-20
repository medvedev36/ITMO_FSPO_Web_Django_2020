from django.shortcuts import render
from django.http import Http404 

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import *
from .forms import *

# Create your views here.

def owner(request, owner_id):
  try:
    owner = Owner.objects.get(pk=owner_id)

  except Owner.DoesNotExist:
    raise Http404("Owner doesn't exists") 
  
  return render(request, 'owner/owner.html', {'owner': owner})


def ownerList(request):
  return render(request, 'owner/ownerList.html', {'owners': Owner.objects.all()})

def ownerCreate(request):
  form = OwnerForm(request.POST or None)

  if form.is_valid():
    form.save()

  return render(request, "owner/ownerCreate.html", {'form': form})

def car(request, car_id):
  try:
    car = Car.objects.get(pk=car_id)

  except Car.DoesNotExist:
    raise Http404("Car doesn't exists") 
  
  return render(request, 'car/car.html', {'car': car})

class CarList(ListView):
  model = Car
  template_name = 'car/carlist.html'

class CarCreate(CreateView):
  model = Car
  fields = ["id", "brand", "model", "color", "num"]
  template_name = 'car/carCreate.html'


