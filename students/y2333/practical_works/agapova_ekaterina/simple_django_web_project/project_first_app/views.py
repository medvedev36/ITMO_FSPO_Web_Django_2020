from django.http import Http404
from django.shortcuts import render
from .models import Owner


def details(request, id):

    try:
        owner = Owner.objects.get(pk=id)
    except Owner.DoesNotExist:
        raise Http404("Owner doesn't exist")
    return render(request, 'details.html', {'owner': owner})
