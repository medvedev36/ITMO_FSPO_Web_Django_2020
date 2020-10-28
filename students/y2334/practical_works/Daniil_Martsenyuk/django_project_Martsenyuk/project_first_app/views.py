from django.shortcuts import render
from project_first_app.models import *
from django.http import Http404


def detail(request, person_id):
    try:
        p = Owner.objects.get(pk=person_id)
    except Owner.DoesNotExist:
        raise Http404("This person does not exist")
    return render(request, 'detail.html', {'person': p})
