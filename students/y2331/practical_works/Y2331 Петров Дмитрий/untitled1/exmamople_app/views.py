from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from exmamople_app.models import User
from .models import Avtom
from .forms import Useradd
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


def list_v(request):
    context = {}
    context["dataset"] = User.objects.all()
    return render(request, "list_v.html", context)


class AvtomList(ListView):
    model = Avtom


def create_view(request):
    context = {}
    form = Useradd(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)


class Avtocreate(CreateView):
    model = Avtom
    fields = ['mark', 'model', 'dateo']
