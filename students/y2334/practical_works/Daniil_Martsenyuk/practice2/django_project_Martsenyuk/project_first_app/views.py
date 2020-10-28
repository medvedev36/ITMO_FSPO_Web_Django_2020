from django.shortcuts import render
from project_first_app.models import *
from django.http import Http404
from django.views.generic.list import ListView
from project_first_app.forms import *
from django.views.generic.edit import CreateView


def detail(request, person_id):
    try:
        p = Owner.objects.get(pk=person_id)
    except Owner.DoesNotExist:
        raise Http404("This person does not exist")
    return render(request, 'detail.html', {'person': p})


def all_owners(request):
    context = {
        'owners': Owner.objects.all(),
    }
    return render(request, 'allOwners.html', context)


class Cars(ListView):
    model = Auto


def create_owner(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form

    return render(request, 'owner_form.html', context)


class AutosCreate(CreateView):
    model = Auto
    fields = ['mark', 'model', 'color', 'gov_number']

