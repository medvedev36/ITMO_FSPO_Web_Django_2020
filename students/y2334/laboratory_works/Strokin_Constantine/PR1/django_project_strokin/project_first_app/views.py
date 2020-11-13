from django.shortcuts import render
from .models import Owner
from django.http import HttpResponseNotFound


def Owner_(request, id):
    try:
        owner = Owner.objects.get(id = id)
        return render(request,"Owner.html", {"owner": owner})
    except Owner.DoesNotExist:
        return HttpResponseNotFound("<h2>Owner not found</h2>")


def Owners_(request):
    context ={}
    context["dataset"] = Owner.objects.all()
    return render(request, "Owners.html", context)
