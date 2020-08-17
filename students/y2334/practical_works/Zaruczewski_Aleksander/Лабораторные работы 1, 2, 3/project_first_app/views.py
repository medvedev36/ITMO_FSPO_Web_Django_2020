from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, CreateView
from .models import *
from .forms import *


def details(request, owner_id):
    try:
        o = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': o})


def owner_view(request):
    context = {"dataset": Owner.objects.all()}
    return render(request, "owner_view.html", context)


def owner_form_view(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "owner_form_view.html", context)


class Cars(ListView):
    model = Car


class CarCreate(CreateView):
    model = Car
    fields = ['license_plate', 'brand', 'model', 'color']
