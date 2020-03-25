from django.shortcuts import render
from django.http import HttpResponse
import datetime
def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body>It's now %s.</body></html>" % now
    return HttpResponse(html)
# Create your views here.
from django.http import Http404
from django.shortcuts import render
from .models import User

def detail(request, pass_num):
    try:
        p = User.objects.get(pk=pass_num)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'owner.html', {'User': p})
