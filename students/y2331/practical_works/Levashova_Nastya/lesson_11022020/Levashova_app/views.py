from django.shortcuts import render
from django.http import HttpResponse
import datetime

from django.http import Http404
from django.shortcuts import render
from django.urls import reverse

from .models import User
from django.views.generic.list import ListView
from .models import Car
from .forms import UserForm
from django.views.generic.edit import CreateView

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def user(request, passport_ID):
    try:
        p = User.objects.get(pk=passport_ID)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'users.html', {'poll': p})

def list_view(request):
    context = {}
    context["dataset"] = User.objects.all()
    return render(request, "User.html", context)

class cars_list(ListView):
    model = Car

def create_view(request):
    context = {}
    form = UserForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)

class CarCreate(CreateView):
    model = Car
    fields = ['car_brand', 'car_model', "car_year", "state_number"]
    success_url = '/car_form'

