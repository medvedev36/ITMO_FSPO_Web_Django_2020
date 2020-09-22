from django.shortcuts import render
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Owner, Auto
from .forms import OwnerForm


def detail(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exists")
    return render(request, 'owner.html', {'owner': owner})


def allOwners(request):
    owners = Owner.objects.all()
    return render(request, 'ownersInfo.html', {'owners': owners})


class AutoList(ListView):
    model = Auto
    template_name = 'autosInfo.html'
    context_object_name = 'autos'


def createOwner(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'createOwner.html', context)


class AutoCreate(CreateView):
    model = Auto
    template_name = 'createAuto.html'
    fields = ['mark', 'model', 'color', 'state_number']
    success_url = '.'