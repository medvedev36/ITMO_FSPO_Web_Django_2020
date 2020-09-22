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
        'products': Product.objects.all()[:10],
        'providers': Provider.objects.all()[:10],
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
        'providers': Provider.objects.all()[:10],
        'deals': Deals.objects.all()[:10],
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

        'form': UserUpdateForm(instance=request.user)
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


class ProductList(ListView):
    model = Product
    template_name = 'Base/product_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['products'] = Product.objects.all()[:10]
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'Base/product_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['product'] = Product.objects.all()[:10]
        context['suppliers'] = Supplier.objects.all()[:10]
        context['deals'] = Deals.objects.all()[:10]
        return context


class ProviderList(ListView):
    model = Provider
    template_name = 'Base/provider_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['providers'] = Provider.objects.all()[:10]
        return context


class ProviderDetail(DetailView):
    model = Provider
    template_name = 'Base/provider_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['providers'] = Provider.objects.all()[:10]
        return context


class BrokerList(ListView):
    model = Broker
    template_name = 'Base/broker_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class DealForm(CreateView):
    model = Deals
    template_name = 'Base/deal_form.html'
    fields = ['code_deal', 'date_deal', 'col_sold', 'view_prod', 'br_name', 'prod_name']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['confirm'] = 'Оформить Сделку'

        return context