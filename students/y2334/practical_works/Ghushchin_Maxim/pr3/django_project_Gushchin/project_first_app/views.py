from django.shortcuts import render, redirect
from project_first_app.models import *
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from project_first_app.forms import *


def view_users(request, pk):
    user = get_object_or_404(Person, pk=pk) #Person.objects.get(2)

    context = {
        'user': user,
    }

    return render(request, 'user.html', context)


def all_users(request):
    context = {
        'users': Person.objects.all(),
    }
    return render(request, 'users.html', context)


class Cars(ListView):
    model = Auto


def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()

    form = PersonForm()
    context = {
        'form': form
    }

    return render(request, 'form_user.html', context)


class AutosCreate(CreateView):
    model = Auto
    fields = ['mark', 'model', 'color', 'gov_number']
    success_url = 'cars'
