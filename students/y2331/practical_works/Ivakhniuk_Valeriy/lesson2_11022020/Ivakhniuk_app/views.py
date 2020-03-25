from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

from django.http import Http404
from django.shortcuts import render
from .models import Auto
from .models import User
from .models import DriverLicense
from .models import Usage

def detail(request, poll_id):
    try:
        p = User.objects.get(pk=poll_id)
    except Auto.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'owners.html', {'poll': p})