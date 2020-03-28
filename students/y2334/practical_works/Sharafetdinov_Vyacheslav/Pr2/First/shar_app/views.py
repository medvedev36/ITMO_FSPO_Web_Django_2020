from django.http import Http404
from django.shortcuts import render

from django.views.generic.list import ListView

from shar_app.models import Owner
from shar_app.models import Auto

def default(request):
    return render(request, 'default.html')

def OwnerInfo(request, owner_id):
    try:
        ow = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Владелец не найден")
    return render(request, 'owner.html', {'owner': ow})

def list_owners(request):
    list={}
    list["objects"] = Owner.objects.all()
    return render(request, 'list_owners.html', list)

class list_autos(ListView):
    model = Auto
    template_name = "list_autos.html"