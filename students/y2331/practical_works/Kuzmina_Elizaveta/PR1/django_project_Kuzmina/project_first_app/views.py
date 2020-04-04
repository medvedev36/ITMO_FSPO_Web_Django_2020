from django.shortcuts import render
from django.http import Http404
from project_first_app.models import CarOwner


def detail(request, CarOwner_id):
    try:
        p = CarOwner.objects.get(pk=CarOwner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'Owner.html', {'owner': p})


from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It's now %s.</body></html>" % now
    return HttpResponse(html)
