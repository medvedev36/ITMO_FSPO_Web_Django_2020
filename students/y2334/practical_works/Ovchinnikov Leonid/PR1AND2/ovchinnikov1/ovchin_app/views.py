from django.http import Http404
from django.shortcuts import render
from ovchin_app.models import Owner,Car
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import OwnerForm

def details(request, owner_id):
    try:
       owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner/details.html', {'owner': owner})

def list_owner(request):
    context ={}

    context["dataset"] = Owner.objects.all()
    return render(request, "owner/list_onwers.html", context)

class  CarList(ListView):
    template_name = "owner/list_cars.html"
    model = Car

def create_owner(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request,"owner/create_owner.html", context)

class CarCreate(CreateView):
    template_name = "owner/create_car.html"
    success_url = "."
    model = Car
    fields = ['mark', 'model', 'year']
