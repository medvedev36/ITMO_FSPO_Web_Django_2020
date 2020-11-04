from django.http import Http404
from django.shortcuts import render
from .models import Owner, Car
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import OwnersForm


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


def owner_form(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = OwnersForm(
        request.POST or None)  # создаем экземпляр формы, отсылаем в него данные из формы (из полей в браузере)
    if form.is_valid():  # Проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "project_first_app/owner_form.html", context)


class CarsForm(CreateView):
    # specify the model for create view
    model = Car
    success_url = 'carform'

    # specify the fields to be displayed

    fields = ['marka', 'model', 'carNumber', 'color']