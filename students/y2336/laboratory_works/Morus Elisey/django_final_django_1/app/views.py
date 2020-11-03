from django.db.models import Max, Count, Sum
from django.http import HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .models import *
from .forms import *


class MyRegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/accounts/login/"
    template_name = "signup.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


def logout(request):
    return render(request, "logout.html")


def top(request):
    buy = Buy.objects.filter().values('disk').order_by()
    disc = buy[0]
    context = {}
    print(disc)
    return render(request, "top.html", {"disc": disc})


def disc(request):
    context = {}
    context["data_d"] = Disk.objects.all()
    return render(request, 'disc.html', context)


def singer(request):
    context = {}
    context["data_s"] = Singer.objects.all()
    return render(request, 'singer.html', context)


def sing(request):
    context = {}
    context["data_s"] = Sing.objects.all()
    return render(request, 'sing.html', context)


def disc_add(request):
    context = {}
    form = Disk_form(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    context['data_s'] = Sing.objects.all()
    return render(request, "disk_add.html", context)


def sing_add(request):
    context = {}
    form = Sing_form(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    context['data_s'] = Singer.objects.all()
    return render(request, "sing_add.html", context)


def singer_add(request):
    context = {}
    form = Singer_form(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "singer_add.html", context)


def disc_delete(request, disc_id):
    try:
        c = Disk.objects.get(id=disc_id)
        c.delete()
        context = {}
        context["data_s"] = Disk.objects.all()
        return render(request, 'disc.html', context)
    except Disk.DoesNotExist:
        return HttpResponseNotFound("<h2>Disc not found</h2>")


def info_sing(request, disc_name):
    try:
        context = {}
        context["sing"] = Sing.objects.get(name=disc_name)
        return render(request, 'info_sing.html', context)
    except Disk.DoesNotExist:
        return HttpResponseNotFound("<h2>Sing not found</h2>")


def disc_edit(request, disc_id):
    try:
        data_d = Disk.objects.get(id=disc_id)
        data_s = Sing.objects.all()
        if request.method == "POST":
            data_d.sing = request.POST.get("sing")
            data_d.production_date = request.POST.get("production_date")
            data_d.price = request.POST.get("price")
            data_d.producer = request.POST.get("producer")
            data_d.save()
            return HttpResponseRedirect("/disc")
        else:
            return render(request, "disc_edit.html", {"data_d": data_d, "data_s": data_s})
    except Disk.DoesNotExist:
        return HttpResponseNotFound("<h2>Disc not found</h2>")


def buy(request):
    context = {}
    form = Buy_form(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    context["data_s"] = Disk.objects.all()
    return render(request, "buy.html", context)