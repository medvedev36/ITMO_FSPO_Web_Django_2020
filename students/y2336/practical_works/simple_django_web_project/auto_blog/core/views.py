from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from .models import Vehicle
from .forms import OwnerForm

# Create your views here.
def index(request, fk):
    try: 
        content = {
            'user': User.objects.get(id=fk),
        }
    except User.DoesNotExist:
        return HttpResponse(status=404)
    vehicles = Vehicle.objects.filter(possession__owner=content['user'])
    content['vehicles'] = vehicles
    return render(request, 'core/profile.html', content)

def list_owner(request):
    content = {
        'users': User.objects.all()
    }
    return render(request, 'core/list_owner.html', content)

def form_owner(request):
    form = OwnerForm(request.POST)
    if form.is_valid():
        form.save()
    content = {
        'form': form,
    }
    return render(request, 'core/form_owner.html', content)


class VehicleListView(ListView):
    model = Vehicle
    template_name = 'core/list_vehicle.html' 
    context_object_name = 'vehicles'


class VehicleCreate(CreateView):
    model = Vehicle
    template_name = 'core/form_vehicle.html' 
    fields = [
            'model',
            'brand',
            'color',
            'license_plate',
    ]
    success_url = '/vehicle/all'