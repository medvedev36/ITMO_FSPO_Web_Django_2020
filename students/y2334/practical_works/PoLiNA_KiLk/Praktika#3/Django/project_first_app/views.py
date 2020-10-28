from django.shortcuts import render
from project_first_app.models import Person
from project_first_app.models import Car
from django.views.generic.list import ListView
from .forms import PersonForm
from django.views.generic.edit import CreateView


# Create your views here.


class CarView(ListView):
    model = Car


def list_view(request):
    context = {"dataset": Person.objects.all()}

    return render(request, "list_view.html", context)


def create_view(request):
    context = {}
    form = PersonForm(request.POST or None)

    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


class CarCreate(CreateView):
    model = Car
    fields = [
        'Logo',
        'Color',
        'Model',
        'Number'
    ]
