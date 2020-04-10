from django.http import Http404
from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from shar_app.models import Owner
from shar_app.models import Auto

from shar_app.forms import OwnerForm


def default(request):
    return render(request, 'shar_app/default.html')


def OwnerInfo(request, owner_id):
    try:
        ow = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Владелец не найден")
    return render(request, 'shar_app/owner.html', {'owner': ow})


def list_owners(request):
    list = {}
    list["objects"] = Owner.objects.all()
    return render(request, 'shar_app/list_owners.html', list)


class list_autos(ListView):
    model = Auto
    template_name = "shar_app/list_autos.html"


def form_owner(request):
    content = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    content['form'] = form
    return render(request, "shar_app/owner_form.html", content)


class form_auto(CreateView):
    model = Auto
    fields = [
        "mark",
        "model",
        "year"
    ]
