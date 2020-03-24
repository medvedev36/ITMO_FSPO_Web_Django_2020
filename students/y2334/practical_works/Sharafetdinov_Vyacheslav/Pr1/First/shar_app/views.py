from django.http import Http404
from django.shortcuts import render
from shar_app.models import Owner

def detail(request, owner_id):
    try:
        ow = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owners/detail.html', {'owner': ow})




