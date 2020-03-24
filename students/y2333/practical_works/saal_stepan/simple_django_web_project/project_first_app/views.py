from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render
from .models import Owner


def details(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owners/details.html', {'owner': owner})
