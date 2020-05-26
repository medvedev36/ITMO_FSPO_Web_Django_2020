from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic.list import ListView
import datetime
from .forms import UserForm
from django.views.generic.edit import CreateView


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
    return render(request, 'owner.html', {'poll': p})


def list_view(request):
    context = {}
    context["dataset"] = User.objects.all()
    return render(request, "Owners_list.html", context)


class AutoList(ListView):
    model = Auto


def create_view(request):
    context = {}
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_user_view.html", context)


class AutoForm(CreateView):
    model = Auto

    fields = [
        "car_brand",
        "car_model",
        "car_year",
    ]
    success_url = '/add_auto'
