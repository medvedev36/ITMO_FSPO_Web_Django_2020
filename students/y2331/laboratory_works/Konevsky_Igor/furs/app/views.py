from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *


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


def buyerlist(request):
    buyers = Buyer.object.all()
    return render(request, "app/buyer_list.html", {"buyers": buyers})


def purchaselist(request):
    purchases = Purchase.object.all()
    return render(request, "app/purchase_list.html", {"purchases": purchases})


class FarmCreate(CreateView):
    model = Farm
    fields = ['adress', 'surname', 'phone']


class FurCreate(CreateView):
    model = Fur
    fields = ['name', 'sort', 'farm']


class BuyerCreate(CreateView):
    model = Buyer
    fields = ['name', 'category']


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['amount', 'buyer', 'fur']


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


class BuyerUpdate(UpdateView):
    model = Buyer
    fields = ['name', 'category']
    template_name_suffix = '_update'
    success_url = '/buyer_list/'


class PurchaseUpdate(UpdateView):
    model = Purchase
    fields = ['amount', 'buyer', 'fur']
    template_name_suffix = '_update'
    success_url = '/purchase_list/'


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


def buyerdelete(request, pk):
    buyer = get_object_or_404(Buyer, buyer_id=pk)
    buyer.delete()
    return render(request, "app/buyer_delete.html", {"buyer": buyer})


def purchasedelete(request, pk):
    purchase = get_object_or_404(Purchase, purchase_id=pk)
    purchase.delete()
    return render(request, "app/purchase_delete.html", {"purchase": purchase})
