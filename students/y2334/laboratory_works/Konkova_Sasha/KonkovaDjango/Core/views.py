from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from random import randint
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from User.forms import AddFundsForm, PurchaseForm
from .forms import FuelInStationForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .forms import *
from .models import *

# Create your views here.
def home(request):
    context = {
        'avg_prices': FuelInStation.objects.values('fuel').annotate(avg=Avg('price'))
    }
    for obj in context['avg_prices']:
        obj['fuel'] = Fuel.objects.get(pk=obj['fuel'])
    return render(request, 'Core/home.html', context)

@login_required
def add_funds(request):
    if request.method == 'POST':
        form = AddFundsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AddFundsForm(instance=request.user)
    return render(request, 'Core/add_funds.html', {'form': form})

@login_required
def buy_fuel(request, station, fuel):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        form.instance.client = request.user
        form.instance.fuel_in_station = get_object_or_404(FuelInStation, fuel_id=fuel, station_id=station)
        if form.is_valid():
            form.save()
            request.user.balance -= float(form.data['amount']) * float(form.instance.fuel_in_station.price)
            request.user.save()
            return redirect('user-purchase', request.user.id)
    else:
        form = PurchaseForm()
    return render(request, 'Core/purchase_create.html', {'form': form})


@login_required
def add_fuel_to_station(request, station):
    if request.method == 'POST':
        form = FuelInStationForm(request.POST)
        form.instance.station = get_object_or_404(FuelStation, pk=station)
        print("hello")
        if form.is_valid():
            form.save()
            # request.user.balance -= float(form.data['amount']) * float(form.instance.fuel_in_station.price)
            # request.user.save()
            return redirect('fuelstation-detail', form.instance.station.id)
    else:
        form = FuelInStationForm()
    print(type(form))
    return render(request, 'Core/fuel_in_station_create.html', {'form': form})


class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = get_user_model()
    success_url = '/home/'

    def test_func(self):
        user = self.get_object()
        return user == self.request.user


class ClientPurchaseList(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = get_user_model()
    template_name = 'Core/purchase_list.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchases'] = Purchase.objects.filter(client=context['user']).order_by('-date')
        return context
    
    def test_func(self):
        user = self.get_object()
        return user == self.request.user


class FuelStationListView(ListView):
    model = FuelStation
    template_name = 'Core/fuelstation_list.html'
    context_object_name = 'fuelstations'


class FuelStationCreateView(LoginRequiredMixin, CreateView):
    model = FuelStation
    template_name = 'Core/fuelstation_create.html'
    fields = ['name', 'provider', 'address']
    success_url = reverse_lazy('fuelstation-list')


class FuelStationDetailView(DetailView):
    model = FuelStation
    template_name = 'Core/fuelstation_detail.html'
    context_object_name = 'station'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fuels'] = FuelInStation.objects.filter(station=context['station'])
        # if self.request.method == 'POST':
        #     print('hello')
        #     pass
        context['form'] = FuelInStationForm()
        return context


class FuelProviderListView(ListView):
    model = FuelProvider
    template_name = 'Core/fuelprovider_list.html'
    context_object_name = 'providers'


class FuelProviderDetailView(DetailView):
    model = FuelProvider
    template_name = 'Core/fuelprovider_detail.html'
    context_object_name = 'provider'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stations'] = FuelStation.objects.filter(provider=context['provider'])
        context['time'] = '{}:{} - {}:{}'.format(randint(8, 9), randint(10, 59), randint(22, 23), randint(10, 59))
        return context


class FuelDetailView(DetailView):
    model = Fuel
    template_name = 'Core/fuel_detail.html'
    context_object_name = 'fuel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stations'] = FuelInStation.objects.filter(fuel=context['fuel']).order_by('price')
        return context
