from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions

from adApp.serializers import *
from adApp.models import *

class TVShows(APIView):
    permission_classes = [permissions.AllowAny, ]

    # Функция про получения инофрмации о программах
    def get(self, request):
        shows = TVShow.objects.all()
        serializer = TVShow_Serializers(shows, many=True)
        return Response({"data": serializer.data})

class AddTVShows(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    # Функция для добавления новой программы
    def post(self, request):
        show = AddTVShow_Serializers(data=request.data)
        if show.is_valid():
            show.save()
            return Response(status=201)
        else:
            return Response(status=400)

class Advertisings(APIView):
    permission_classes = [permissions.AllowAny, ]

    # Функция для получения информации о роликах
    def get(self, request):
        advertising = Advertising.objects.all()
        serializer = Advertising_Serializers(advertising, many=True)
        return Response({"data": serializer.data})

class AddAdvertisings(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    # Функция для добавления ролика
    def post(self, request):
        ad = AddAdvertising_Serializers(data=request.data)
        if ad.is_valid():
            ad.save()
            return Response(status=201)
        else:
            return Response(status=400)

class PutAdvertisings(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    # Функция для изменения ролика
    def put(self, request, pk):
        saved_ad = get_object_or_404(Advertising.objects.all(), pk=pk)
        serializer = AddAdvertising_Serializers(instance=saved_ad, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

class AdBreaks(APIView):
    permission_classes = [permissions.AllowAny, ]

    # Функция для получения информации о показах
    def get(self, request):
        adBreak = AdBreak.objects.all()
        serializer = AdBreak_Serializers(adBreak, many=True)
        return Response({"data": serializer.data})

class AddAdBreaks(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    # Функция для добавления показа
    def post(self, request):
        adbreak = AddAdBreak_Serializers(data=request.data)
        if adbreak.is_valid():
            adbreak.save()
            return Response(status=201)
        else:
            return Response(status=400)

class Channels(APIView):
    permission_classes = [permissions.AllowAny, ]

    # Функция для получения информации о каналах
    def get(self, request):
        channel = Channel.objects.all()
        serializer = Channel_Serializers(channel, many=True)
        return Response({"data": serializer.data})

class Advertisers(APIView):
    permission_classes = [permissions.AllowAny, ]

    # Функция для получения информации о рекламных компаниях
    def get(self, request):
        adver = Advertiser.objects.all()
        serializer = Advertiser_Serializers(adver, many=True)
        return Response({"data": serializer.data})
