from django.http import Http404


from django.shortcuts import render, get_object_or_404
# from models.py import Owner
from .models import Owner


def owner_dossier(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    return render(request, 'django_project_primachenko/owner_dossier.html', {'owner': owner})

