from django.http import Http404
from django.shortcuts import render
from .models import Owner, Car
from django.views.generic.list import ListView


def details(request, id):

    try:
        owner = Owner.objects.get(pk=id)
    except Owner.DoesNotExist:
        raise Http404("Owner doesn't exist")
    return render(request, 'project_first_app/owner_details.html', {'owner': owner})


def owner_list(request):

    owners = Owner.objects.all()
    return render(request, 'project_first_app/owner_list.html', {'owners': owners})


class CarList(ListView):

    model = Car
