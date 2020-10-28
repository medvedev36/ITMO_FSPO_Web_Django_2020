from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.views import View
from .models import *
from .forms import *


def disk_list(request):
    disks = Disk.objects.all()
    return render(request, "disk_list.html", context={"disk_list": disks})


def addDisk(request):
    form = DiskForm(request.POST or None)
    if form.is_valid():
        new_order = form.save()
        new_order.incomeCost = form.cleaned_data['incomeCost']
        new_order.idMusic = form.cleaned_data['idMusic']
        new_order.save()
        return HttpResponseRedirect('/')
    return render(request, "Add.html", {'form': form})


def addAuthor(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        new_order = form.save()
        new_order.name = form.cleaned_data['name']
        new_order.dateOfBirth = form.cleaned_data['dateOfBirth']
        new_order.save()
    return render(request, "Add.html", {'form': form})


def addMusic(request):
    form = MusicForm(request.POST or None)
    if form.is_valid():
        new_order = form.save()
        new_order.idAuthor = form.cleaned_data['idAuthor']
        new_order.musicName = form.cleaned_data['musicName']
        new_order.save()
    return render(request, "Add.html", {'form': form})


def addProducer(request):
    form = ProducerForm(request.POST or None)
    if form.is_valid():
        new_order = form.save()
        new_order.name = form.cleaned_data['name']
        new_order.country = form.cleaned_data['country']
        new_order.save()
    return render(request, "Add.html", {'form': form})


def editPro(request, id):
    pro = Producer.objects.get(id=id)
    if request.method == "POST":
        pro.name = request.POST.get("name")
        pro.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "editPro.html", {"pro": pro})


def editAuthor(request, id):
    author = Author.objects.get(id=id)
    if request.method == "POST":
        author.name = request.POST.get("name")
        author.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "editAuthor.html", {"author": author})


def editCost(request, id):
    disk = Disk.objects.get(id=id)
    if request.method == "POST":
        disk.incomeCost = request.POST.get("incomeCost")
        disk.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "edit.html", {"disk": disk})


def editMusic(request, id):
    music = Music.objects.get(id=id)
    if request.method == "POST":
        music.musicName = request.POST.get("musicName")
        music.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "editMusic.html", {"music": music})


def delete(request, id):
    try:
        disk = Disk.objects.get(id=id)
        disk.delete()
        return HttpResponseRedirect('/')
    except Disk.DoesNotExist:
        return HttpResponseNotFound("<h1>Disk not found</h1>")

