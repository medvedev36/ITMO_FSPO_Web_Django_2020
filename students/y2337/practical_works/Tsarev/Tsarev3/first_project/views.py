from django.shortcuts import render, get_object_or_404
from .models import Owner, Auto
from .forms import OwnerForm, AutoForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView


# Create your views here.

def auto_detail(request, auto_id):
    auto = get_object_or_404(Auto, pk=auto_id)
    return render(request, 'detailauto.html', {'auto': auto})

def detail(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    return render(request, 'detailown.html', {'owner': owner})


def ownerview(request):
    return render(request, 'ownerview.html', {'owners_list': Owner.objects.all()})


def autoview(request):
    return render(request, 'autoview.html', {'auto_list': Auto.objects.all()})


def create_owner(request):
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "create_owner.html", {'form': form})


class AutoList(ListView):
    model = Auto
    template_name = 'autolist.html'


class AutoCreate(CreateView):
    model = Auto
    form_class = AutoForm
    template_name = 'create_auto.html'
