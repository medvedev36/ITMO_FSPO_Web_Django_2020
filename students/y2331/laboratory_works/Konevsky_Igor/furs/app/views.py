from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *


class LogoutView(View):
    def get(self, request):
        logout(request)

        return HttpResponseRedirect("/")


class RegisterView(FormView):
    form_class = UserCreationForm

    success_url = "/accounts/login"

    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()

        return super(RegisterView, self).form_valid(form)


def home(request):
    return render(request, "app/home.html")


def farmlist(request):
    farms = Farm.object.all()
    return render(request, "app/farm_list.html", {"farms": farms})


def furlist(request):
    furs = Fur.object.all()
    return render(request, "app/fur_list.html", {"furs": furs})


def coatlist(request):
    coats = Coat.object.all()
    return render(request, "app/coat_list.html", {"coats": coats})


def purchaselist(request):
    purchases = Purchase.object.all().filter(user_id=request.user.id)
    return render(request, "app/profile.html", {"purchases": purchases})


class FarmCreate(CreateView):
    model = Farm
    fields = ['adress', 'surname', 'phone']


class FurCreate(CreateView):
    model = Fur
    fields = ['name', 'sort', 'farm']


class CoatCreate(CreateView):
    model = Coat
    fields = ['name', 'price', 'fur']


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['coat']


class FarmUpdate(UpdateView):
    model = Farm
    fields = ['adress', 'surname', 'phone']
    template_name_suffix = '_update'
    success_url = '/farm_list/'


class FurUpdate(UpdateView):
    model = Fur
    fields = ['name', 'sort', 'farm']
    template_name_suffix = '_update'
    success_url = '/fur_list/'


class CoatUpdate(UpdateView):
    model = Coat
    fields = ['name', 'price', 'fur']
    template_name_suffix = '_update'
    success_url = '/coat_list/'


# class FarmDelete(DeleteView):
# model = Farm
# success_url = reverse_lazy('/farm_list/')

def farmdelete(request, pk):
    farm = get_object_or_404(Farm, farm_id=pk)
    farm.delete()
    return render(request, "app/farm_delete.html", {"farm": farm})


def furdelete(request, pk):
    fur = get_object_or_404(Fur, fur_id=pk)
    fur.delete()
    return render(request, "app/fur_delete.html", {"fur": fur})


def coatdelete(request, pk):
    coat = get_object_or_404(Coat, coat_id=pk)
    coat.delete()
    return render(request, "app/coat_delete.html", {"coat": coat})


def purchasedelete(request, pk):
    purchase = get_object_or_404(Purchase, purchase_id=pk)
    purchase.delete()
    return render(request, "app/purchase_delete.html", {"purchase": purchase})


def buy(request, pk):
    coat = get_object_or_404(Coat, coat_id=pk)
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_id = request.user.id
            form.coat = coat
            form.save()
            return redirect("/")
    else:
        form = PurchaseForm()
    return render(request, "app/coat_buy.html", {"coat": coat, "form": form})


def addreview(request, pk):
    coat = get_object_or_404(Coat, coat_id=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.text = form.text
            form.coat = coat
            form.save()
            return redirect("/")
    else:
        form = ReviewForm()
    return render(request, "app/review_form.html", {"coat": coat, "form": form})


def reviewlist(request, pk):

    reviews = Review.object.all().filter(coat_id = pk)
    return render(request, "app/reviews.html", {"reviews": reviews})
