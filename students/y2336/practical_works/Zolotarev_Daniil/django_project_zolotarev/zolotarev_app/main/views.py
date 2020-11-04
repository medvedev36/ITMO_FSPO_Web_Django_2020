from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from .models import Vehicle
from .forms import OwnerForm
from django.contrib.auth import get_user_model

# Create your views here.
def index(request, fk):
    try: 
        content = {
            'user': get_user_model().objects.get(id=fk),
        }
    except get_user_model().DoesNotExist:
        return HttpResponse(status=404)
    vehicles = Vehicle.objects.filter(possession__owner=content['user'])
    content['vehicles'] = vehicles
    return render(request, 'main/profile.html', content)

def list_owner(request):
    content = {
        'users': get_user_model().objects.all()
    }
    return render(request, 'main/list_owner.html', content)

def form_owner(request):
    form = OwnerForm(request.POST)
    if form.is_valid():
        form.save()
    content = {
        'form': form,
    }
    return render(request, 'main/form_owner.html', content)


class VehicleListView(ListView):
    model = Vehicle
    template_name = 'main/list_vehicle.html'
    context_object_name = 'vehicles'


class VehicleCreate(CreateView):
    model = Vehicle
    template_name = 'main/form_vehicle.html'
    fields = [
            'model',
            'brand',
            'color',
            'license_plate',
    ]
    success_url = '/vehicle/all'