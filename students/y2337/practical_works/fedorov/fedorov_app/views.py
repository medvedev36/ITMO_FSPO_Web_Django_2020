from datetime import datetime

from django.http import Http404
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.list import ListView

# Create your views here.
from fedorov_app.models import *
from .forms import *


def details(request, id):
    try:
        owner = Owner.objects.get(pk=id)
    except Owner.DoesNotExist:
        return Http404
    return render(request, "owner/detail.html", {'owner': owner})


def owner_list(request):
    return render(request, 'owner/list.html', {'owners': Owner.objects.all()})


def owner_create(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "owner/create_view.html", context)


class CarList(ListView):
    model = Car
    template_name = 'car/list.html'


class CarCreate(CreateView):
    model = Car
    fields = ['id', 'model', 'provider']
    template_name = 'car/create_view.html'
