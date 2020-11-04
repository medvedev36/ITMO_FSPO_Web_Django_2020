from django.shortcuts import render

# Create your views here.
from .models import Owner


def ownerDetails(request, owner_id):
    o = Owner.objects.get(pk=owner_id)
    return render(request, 'ownerDetails.html', {'owner': o})
