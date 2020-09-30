from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import *
from .models import *


def detail_auto(request, auto_id):
    auto = get_object_or_404(Auto, pk=auto_id)
    return render(request, 'detailauto.html', {'auto' : auto})


class AutoList(ListView):
    model = Auto
    template_name = 'autolist.html'


class AutoCreate(CreateView):
    model = Auto
    form_class = AutoForm
    template_name = 'create_auto.html'
# Create your views here.
