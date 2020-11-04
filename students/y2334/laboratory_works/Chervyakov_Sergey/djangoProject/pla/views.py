from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import *

from .models import *


# Create your views here.


def home(request):
    context = {

    }
    return render(request, 'temp.html', context)


class attraction_list(ListView):
    model = Attraction
    template_name = 'pla/attraction_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Attraction'] = Attraction.objects.all()[:10]
        return context


class attraction_detail(DetailView):
    model = Attraction
    template_name = 'pla/attraction_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Attraction'] = Attraction.objects.all()[:10]
        context['Relationship'] = Relationship.objects.all()[:10]
        context['Price'] = Price.objects.all()[:10]
        context['Platform'] = Platform.objects.all()[:10]
        return context


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
        'attraction': Attraction.objects.all()[:10],
    }
    return render(request, 'pla/form.html', context)


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
    return render(request, 'pla/profile.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'pla/form.html', {'form': form, 'confirm': 'Зарегистрироваться'})


def my_logout(request):
    logout(request)
    return redirect('home')


class platform_list(ListView):
    model = Platform
    template_name = 'pla/platform_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Platform'] = Platform.objects.all()[:10]
        return context


class deal_form(CreateView):
    model = Operation
    template_name = 'pla/deal_form.html'
    fields = ['kids', 'adults', 'privilege', 'Relationship_id']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['confirm'] = 'Оформить'

        return context
