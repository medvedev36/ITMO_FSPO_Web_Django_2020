from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from project_first_app.models import Owner
from project_first_app.models import Car
from project_first_app.forms import OwnerForm


def details(request, owner_id):
    try:
        o = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': o})


def owner_view(request):
    context = {}
    context["dataset"] = Owner.objects.all()
    return render(request, "owner_view.html", context)


class Cars(ListView):
    model = Car


def owner_form_view(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "owner_form_view.html", context)


class CarView(CreateView):
    model = Car
    fields = ['number', 'brand', 'model', 'color']
