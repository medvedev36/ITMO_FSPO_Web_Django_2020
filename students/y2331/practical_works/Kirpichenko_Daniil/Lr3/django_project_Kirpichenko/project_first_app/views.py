from django.shortcuts import render
from .models import Owner, Car
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.utils import timezone
# Create your views here.


def detail(request, poll_id):
    try:
        p = Owner.objects.get(pk=poll_id)
    except Owner.DoesNotExists:
        raise Http404("Poll does not exists")
    return render(request, 'project_first_app/owner.html', {'poll_id': p})


class listOwners(ListView):
    model = Owner

class listCars(ListView):
    model = Car

class viewOwners(CreateView):
    model = Owner
    fields = ['first_name','last_name','birth_date','sex', 'drive_license_id', 'newrow']

class viewCars(CreateView):
    model = Car
    fields = ['license_plat','brand','model','color']