from django.shortcuts import render

from django.http import Http404

from Chervyakov_app.models import Person


def detail(request, id_person):
    try:
        p = Person.objects.get(pk=id_person)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, 'HTML/detail.html', {'person': p})
