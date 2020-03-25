from django.http import Http404
from django.shortcuts import render
from bondarev_app.models import Owner

def detail(request, Owner_id):
    try:
        p = Owner.objects.get(pk=Owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': p})