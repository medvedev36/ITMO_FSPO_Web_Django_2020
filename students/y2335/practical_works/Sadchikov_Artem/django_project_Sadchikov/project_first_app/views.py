from django.http import Http404
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Car
from .models import Car_owner
from .forms import CarOwnerForm

def owner(request,car_owner_id):
        try:
                car_owner = Car_owner.objects.get(pk=car_owner_id)
        except Car_owner.DoesNotExist:
                raise Http404("Owner does not exist")
        return render(request, 'owner.html', {'carowner': car_owner})


def create_owner(request):
    context = {}
    form = CarOwnerForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_owner.html", context)

def show_owner(request):
    context = {}
    context["dataset"] = Car_owner.objects.all()
    return render(request, "show_owner.html", context)

class CarCreate(CreateView):
    template_name = "create_car.html"
    success_url = "."
    model = Car
    fields = [ "number","model","color","governmentNumber"]

class ShowCar(ListView):
    template_name = "show_car.html"
    success_url = "."
    model = Car


