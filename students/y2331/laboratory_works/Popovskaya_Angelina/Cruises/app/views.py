from django.contrib.auth import authenticate, login
from django.http import Http404
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .models import *
from .forms import *


def base(request):
    context = {'data_e': Excursion.objects.all()}
    return render(request, 'base.html', context)


def excursion(request, excursion_id):
    context = {'excursion': Excursion.objects.get(pk=excursion_id), 'data_c': Cruise.objects.all()}
    return render(request, 'excursion.html', context)


class MyRegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/accounts/login/"

    template_name = "signup.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


def selling(request, user_id, excursion_id):
    context = {}
    form = Selling_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/base')
    context['data_u'] = User.objects.get(pk=user_id)
    context['data_e'] = Excursion.objects.get(pk=excursion_id)
    context['data_c'] = Cruise.objects.all()
    context['form'] = form
    return render(request, "sell.html", context)


def account(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        context = {'data_u': user, 'data_e': Excursion.objects.all(), 'data_s': Sell.objects.all()}
    except User.DoesNotExist:
        raise Http404("Пользователя не сущетсвует")
    return render(request, 'account.html', context)


def excursion_add(request):
    context = {}
    form = Excursions_form(request.POST or None)
    context['data_c'] = Excursion.objects.all()
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "excursion_add.html", context)


def excursion_delete(request, cassette_id):
    try:
        c = Excursion.objects.get(id=cassette_id)
        c.delete()
        return redirect('/base')
    except Excursion.DoesNotExist:
        return HttpResponseNotFound("<h2>Круиз не найден</h2>")