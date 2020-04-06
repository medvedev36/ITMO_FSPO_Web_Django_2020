from django.shortcuts import render
from project_first_app.models import Owner
from django.http import Http404


def owner(request, owner_id):
    try:
        o = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("No such owner.")
    return render(request, 'owner.html', {'owner':o})