from django.shortcuts import render
from project_first_app.models import *
from django.http import Http404


def detail(request, person_id):
    try:
        p = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("This person does not exist")
    return render(request, 'detail.html', {'person': p})
