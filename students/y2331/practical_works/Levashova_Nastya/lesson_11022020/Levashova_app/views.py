from django.shortcuts import render
from django.http import HttpResponse
import datetime

from django.http import Http404
from django.shortcuts import render
from .models import User

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def user(request, passport_ID):
    try:
        p = User.objects.get(pk=passport_ID)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'user.html', {'poll': p})
# Create your views here.
