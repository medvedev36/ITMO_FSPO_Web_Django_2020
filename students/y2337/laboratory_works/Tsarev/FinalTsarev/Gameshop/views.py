from django.shortcuts import render
from .models import Disc, Genre
from django.views.generic.base import View
# Create your views here.


def genres_list(request):
    genres = Genre.objects.all()
    return render(request, "genre_list.html", context={"genre_list": genres})


def discs_list(request):
    discs = Disc.objects.all()
    return render(request, "disc_list.html", context={"disc_list": discs})


def disc_detail(request, disc_id):
    disc = Disc.objects.get(pk=disc_id)
    return render(request, "disc_detail.html", context={"disc": disc})


def genre_detail(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    return render(request, "genre_detail.html", context={"genre": genre})

#     <img src="{{ disc.url }}" width="600">
