from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404

from .models import *
from .forms import *


def home(request):
    context = {
        'cds': CD.objects.all()[:10],
        'firms': Firm.objects.all()[:10],
        'brokers': Broker.objects.all()[:10],
    }
    return render(request, 'temp.html', context)


def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('.')
    else:
        form = UserLoginForm()
    context = {
        'form': form,
        'confirm': 'Войти',
        'firm': Firm.objects.all()[:10],
        'deal': Deal.objects.all()[:10],
    }
    return render(request, 'Base/form.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {

        'form': UserUpdateForm(instance=request.user),
        'deals': Deal.objects.all(),
    }
    return render(request, 'Base/profile.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'Base/form.html', {'form': form, 'confirm': 'Зарегистрироваться'})


def my_logout(request):
    logout(request)
    return redirect('home')


class CDList(ListView):
    model = CD
    template_name = 'Base/cd_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['cds'] = CD.objects.all()[:10]
        return context


class CDDetail(DetailView):
    model = CD
    template_name = 'Base/cd_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['cd'] = CD.objects.all()[:10]
        context['games'] = Game.objects.all()[:10]
        context['supplies'] = Supply.objects.all()[:10]
        context['deals'] = Deal.objects.all()[:10]
        return context


class FirmList(ListView):
    model = Firm
    template_name = 'Base/firm_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['firms'] = Firm.objects.all()[:10]
        return context


class FirmDetail(DetailView):
    model = Firm
    template_name = 'Base/firm_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['firms'] = Firm.objects.all()[:10]
        return context


class BrokerList(ListView):
    model = Broker
    template_name = 'Base/broker_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class DealForm(CreateView):
    model = Deal
    template_name = 'Base/deal_form.html'
    fields = ['code_deal', 'date_deal', 'quantity_sale', 'br_name', 'cd_name', 'client']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['confirm'] = 'Оформить Сделку'

        return context
