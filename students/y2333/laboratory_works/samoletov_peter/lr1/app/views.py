from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .models import *
from .forms import *


class MyRegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/accounts/login/"

    template_name = "index.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


def logout(request):
    return render(request, "logout.html")


def home(request):
    return render(request, "home.html")

def book_add(request):
    context = {}
    form = BookForm(request.POST or None)
    context['data'] = Book.objects.all()
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "book_add.html", context)


def reader_add(request):
    context = {}
    form = ReaderForm(request.POST or None)
    context['data'] = Reader.objects.all()
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "reader_add.html", context)


def reader_all(request):
    context = {}
    context['data'] = Reader.objects.order_by("name")
    return render(request, 'home.html', context)


def reader(request, reader_id):
    try:
        context = {'data_r': Reader.objects.get(pk=reader_id), 'data_b': Book.objects.all(),
                   'data_c': Card.objects.all()}
    except User.DoesNotExist:
        raise Http404("Пользователя не сущетсвует")
    return render(request, 'account.html', context)


def card_add(request, reader_id):
    context = {}
    form = CardForm(request.POST or None)
    context = {'data_r': Reader.objects.get(pk=reader_id), 'data_b': Book.objects.all(),
               'data_c': Card.objects.all()}
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "card_add.html", context)
# Create your views here.
