from django.shortcuts import render
from django.http import Http404
from django.urls import reverse

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


def list_owners(request):
    context = {}
    context["dataset"] = CarOwner.objects.all()
    return render(request, "AllOwners.html", context)


from django.views.generic.list import ListView
from .models import Car


class list_cars(ListView):
    model = Car


from django.views.generic.edit import CreateView


class view_cars(CreateView):
    model = Car
    fields = ['carMark', 'model', 'color', 'carNumber']

    def get_success_url(self):
        return reverse('view_car')


from .forms import OwnersForm


def owner_view(request):
    context = {}
    form = OwnersForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "OwnerView.html", context)
