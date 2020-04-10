from datetime import datetime

from django.http import Http404
from django.shortcuts import render

# Create your views here.
from fedorov_app.models import *


def details(request, id):
    try:
        owner = Owner.objects.get(pk=id)
    except Owner.DoesNotExist:
        return Http404
    return render(request, "owners/detail.html", {'owner': owner})
