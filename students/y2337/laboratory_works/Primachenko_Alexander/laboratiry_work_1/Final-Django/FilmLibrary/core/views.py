from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def to_menu(request):
    return redirect("menu/")


def menu_view(request):
    return render(request, 'core/menu.html')


def selling_edit(request, id):
    item = CassetteSelling.objects.get(id=id)
    return render(request, 'core/selling/edit.html', {'item': item})

def selling_update(request, id):
    item = CassetteSelling.objects.get(id=id)
    form = SellingForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return redirect("../all/")
    return render(request, 'core/selling/edit.html', {'item': item})


def arriving_edit(request, id):
    item = CassetteArriving.objects.get(id=id)
    return render(request, 'core/arriving/edit.html', {'item': item})

def arriving_update(request, id):
    item = CassetteArriving.objects.get(id=id)
    form = ArrivingForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return redirect("../all/")
    return render(request, 'core/arriving/edit.html', {'item': item})


def cassette_edit(request, id):
    item = Cassette.objects.get(id=id)
    return render(request, 'core/cassette/edit.html', {'item': item})

def cassette_update(request, id):
    item = Cassette.objects.get(id=id)
    form = CassetteForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return redirect("../all/")
    return render(request, 'core/cassette/edit.html', {'item': item})


def provider_edit(request, id):
    item = Provider.objects.get(id=id)
    return render(request, 'core/provider/edit.html', {'item': item})

def provider_update(request, id):
    item = Provider.objects.get(id=id)
    form = ProviderForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return redirect("../all/")
    return render(request, 'core/provider/edit.html', {'item': item})


def seller_edit(request, id):
    item = Seller.objects.get(id=id)
    return render(request, 'core/seller/edit.html', {'item': item})

def seller_update(request, id):
    item = Seller.objects.get(id=id)
    form = SellerForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return redirect("../all/")
    return render(request, 'core/provider/edit.html', {'item': item})


def seller_destroy(request, id):
    to_be_deleted = Seller.objects.get(id=id)
    to_be_deleted.delete()
    return redirect("../all/")


def provider_destroy(request, id):
    to_be_deleted = Provider.objects.get(id=id)
    to_be_deleted.delete()
    return redirect("../all/")


def cassette_destroy(request, id):
    to_be_deleted = Cassette.objects.get(id=id)
    to_be_deleted.delete()
    return redirect("../all/")


def arriving_destroy(request, id):
    to_be_deleted = CassetteArriving.objects.get(id=id)
    to_be_deleted.delete()
    return redirect("../all/")


def selling_destroy(request, id):
    to_be_deleted = CassetteSelling.objects.get(id=id)
    to_be_deleted.delete()
    return redirect("../all/")


def seller_create(request):
    form = SellerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("../all/")
    return render(request, 'core/seller/create.html', {'form': form})


def cassette_create(request):
    form = CassetteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("../all/")
    return render(request, 'core/cassette/create.html', {'form': form})


def provider_create(request):
    form = ProviderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("../all/")
    return render(request, 'core/provider/create.html', {'form': form})


def arriving_create(request):
    form = ArrivingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("../all/")
    return render(request, 'core/arriving/create.html', {'form': form})


def selling_create(request):
    form = SellingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("../all/")
    return render(request, 'core/selling/create.html', {'form': form})


def cassette_all(request):
    return render(request, 'core/cassette/list.html', {'cassette_list': Cassette.objects.all()})


def seller_all(request):
    return render(request, 'core/seller/list.html', {'seller_list': Seller.objects.all()})


def provider_all(request):
    return render(request, 'core/provider/list.html', {'provider_list': Provider.objects.all()})


def arriving_all(request):
    return render(request, 'core/arriving/list.html', {'arriving_list': CassetteArriving.objects.all()})


def selling_all(request):
    return render(request, 'core/selling/list.html', {'selling_list': CassetteSelling.objects.all()})
