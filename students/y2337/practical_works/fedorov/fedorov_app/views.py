from datetime import datetime

from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
from fedorov_app.models import *


def details(request, id):
    try:
        owner = Owner.objects.get(pk=id)
    except Owner.DoesNotExist:
        return Http404
    return render(request, "owner/detail.html", {'owner': owner})


def owner_list(request):
    return render(request, 'owner/list.html', {'owners': Owner.objects.all()})


class CarList(ListView):
    model = Car
    template_name = 'car/list.html'
