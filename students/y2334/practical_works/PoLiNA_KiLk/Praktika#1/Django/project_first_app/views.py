from django.shortcuts import render
from django.http import Http404
from project_first_app.models import Person


# Create your views here.


def detail(request, person_id):
    try:
        p = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, 'owner.html', {'person': p})
