from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import OwnersForm

# Create your views here.
from django.views.generic.list import ListView
from django.http import Http404
from django.shortcuts import render
from .models import Owner, Car


def details(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'project_first_app/owners/details.html', {'owner': owner})


def listOwners(request):
    owners = Owner.objects.all()
    return render(request, 'project_first_app/owners/list.html', {'owners': owners})


class CarsList(ListView):
    model = Car


def owner_form(request):
    context = {}

    form = OwnersForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "project_first_app/owners/form.html", context)


class CarsForm(CreateView):
    model = Car
    success_url = '/car/new'
    fields = ['mark', 'model', 'color', 'number']