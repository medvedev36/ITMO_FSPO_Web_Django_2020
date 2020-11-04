from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.views import View
from .models import *
from .forms import *


def prods_all(request):
    prods = Product.objects.all()
    return render(request, "prods_all.html", context={"prods": prods})


def addProd(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        temp = form.save()
        temp.nameProd = form.cleaned_data['nameProd']
        temp.varProd = form.cleaned_data['varProd']
        temp.priceProd = form.cleaned_data['priceProd']
        temp.idComp = form.cleaned_data['idComp']
        temp.expProd = form.cleaned_data['expProd']
        temp.save()
        return HttpResponseRedirect('/')
    return render(request, "Add.html", {'form': form})


def addComp(request):
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        temp = form.save()
        temp.name = form.cleaned_data['name']
        temp.save()
    return render(request, "Add.html", {'form': form})


def addMackler(request):
    form = MacklerForm(request.POST or None)
    if form.is_valid():
        temp = form.save()
        temp.idMac = form.cleaned_data['idMac']
        temp.surMac = form.cleaned_data['surMac']
        temp.adrMac = form.cleaned_data['adrMac']
        temp.save()
    return render(request, "Add.html", {'form': form})


def editProdName(request, id):
    prod = Product.objects.get(id=id)
    if request.method == "POST":
        prod.nameProd = request.POST.get("nameProd")
        prod.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "editProdName.html", {"Product": prod})

def editProdCost(request, id):
    prod = Product.objects.get(id=id)
    if request.method == "POST":
        prod.priceProd = request.POST.get("priceProd")
        prod.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "editProdCost.html", {"Product": prod})

def editCompany(request, id):
    company = Company.objects.get(id=id)
    if request.method == "POST":
        company.name = request.POST.get("name")
        company.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "editCompany.html", {"Company": company})


def editMackler(request, id):
    mack = Mackler.objects.get(id=id)
    if request.method == "POST":
        mack.surMac = request.POST.get("surMac")
        mack.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "editMack.html", {"Mackler": mack})


def delete(request, id):
    try:
        prod = Product.objects.get(id=id)
        prod.delete()
        return HttpResponseRedirect('/')
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h1>Product not found</h1>")