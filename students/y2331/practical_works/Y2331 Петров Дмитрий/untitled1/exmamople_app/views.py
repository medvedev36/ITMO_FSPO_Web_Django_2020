from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from exmamople_app.models import User
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def detail(request, passport_num):
    try:
        p = User.objects.get(pk=passport_num)
    except User.DoesNotExist:
        raise Http404("User not exists")
    return render(request, 'Users.html', {'User': p})
