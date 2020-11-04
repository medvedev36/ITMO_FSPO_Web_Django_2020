from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.db.models import ObjectDoesNotExist

from random import randint

import datetime

from .models import Car, CarClass, Rent, License
from .forms import UserRegisterForm, CarForm


def index(request):
    return render(request, 'cars/home.html')


def about_us(request):
    return render(request, 'cars/about_us.html')


@login_required()
def profile(request):
    context = {}
    try:
        context['licence'] = License.objects.get(user=request.user)
    except ObjectDoesNotExist:
        pass
    context['cars'] = Rent.objects.filter(client=request.user)
    return render(request, 'auth/profile.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        print(form.errors)
        return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})


class CarListView(ListView):
    model = Car
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        f = Car.objects.all().first()
        cars = Car.objects.all().reverse()
        car = Car.objects.all().last()
        return super().get(request, args, kwargs)


class CarDetailView(DetailView):
    model = Car


class CarClassListView(ListView):
    model = CarClass


class CarClassDetailView(DetailView):
    model = CarClass

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['cars'] = Car.objects.filter(car_class=context['object'])
        return context


class RentCreateView(LoginRequiredMixin, CreateView):
    model = Rent
    fields = ['issue_datetime', 'return_datetime', 'taken_from', 'return_to']

    def has_license(self, request):
        try:
            license_ = License.objects.get(user=self.request.user)
        except ObjectDoesNotExist:
            return False
        return True

    def get(self, request, *args, **kwargs):
        if not self.has_license(request):
            messages.warning(self.request, 'Для аренды машины нужно подтвердить права в личном кабинете')
            return redirect('profile')
        return super().get(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        if not self.has_license(request):
            return HttpResponseForbidden()
        return super().post(request, args, kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        pk = self.kwargs.pop('pk')
        context['car'] = get_object_or_404(Car, id=pk)
        return context

    def form_valid(self, form):
        if form.instance.issue_datetime >= form.instance.return_datetime:
            messages.warning(self.request, 'Машину можно взять минимум на два день!')
            return self.form_invalid(form)
        form.instance.client = self.request.user
        form.instance.car = get_object_or_404(Car, id=self.kwargs.pop('pk'))
        messages.success(self.request, 'Вы успешно арендовали машину')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class LicenseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = License
    fields = ['number', 'date_of_issue', 'type_of_license']

    def test_func(self):
        try:
            license_ = License.objects.get(user=self.request.user)
            return False
        except ObjectDoesNotExist:
            return True

    def form_valid(self, form):
        if form.instance.date_of_issue > datetime.date.today():
            messages.warning(self.request, 'Введите текущие права')
            return self.form_invalid(form)
        form.instance.user = self.request.user
        messages.success(self.request, 'Вы успешно подтвердили свои права')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('profile')


class CarCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Car
    fields = ['car_image', 'model', 'brand', 'color', 'number_plate', 'sits_number', 'car_class']

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        form.instance.car_price = randint(100, 10000) * 1000
        messages.success(self.request, 'Вы успешно добавили автомобиль')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('car-list')
