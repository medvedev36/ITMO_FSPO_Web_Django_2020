from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

# Create your views here.
from .models import Owner, Auto
from .forms import OwnerForm


def ownerDetails(request, owner_id):
    o = Owner.objects.get(pk=owner_id)
    return render(request, 'ownerDetails.html', {'owner': o})


def allOwners(request):
    o = Owner.objects.all()
    return render(request, 'allOwnersInfo.html', {'owners': o})


class AutoView(ListView):
    model = Auto
    template_name = 'allAutosInfo.html'
    context_object_name = 'autos'

    def get_queryset(self):
        return Auto.objects.all()
    # def get(self, request):
    #     a = Auto.objects.all()
    #     return render(request, 'allAutosInfo.html', {'autos': a})


def create_owner(request):
    context = {}
    form = OwnerForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'ownersForm.html', context)

class AutoCreate(CreateView):
    model = Auto
    fields = ["mark", "model", "color", "number"]
    template_name = 'auto_form.html'
    success_url = 'create'
