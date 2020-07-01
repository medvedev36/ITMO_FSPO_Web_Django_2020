from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *

# Create your views here.
class CompetitionListView(ListView):
    model = Competition


class CompetitionDetailView(DetailView):
    model = Competition

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['participants'] = Race.objects.filter(competition=context['object']).order_by('place')
        return context


class CrewListView(ListView):
    model = Crew


class CrewDetailView(DetailView):
    model = Crew

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['competitions'] = Race.objects.filter(crew=context['object'])
        return context


class HippodromeListView(ListView):
    model = Hippodrome


class HippodromeDetailView(DetailView):
    model = Hippodrome

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['competitions'] = Competition.objects.filter(hippodrome=context['object'])
        return context


class JockeyDetailView(DetailView):
    model = Jockey

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['races'] = Race.objects.filter(crew__jockey=context['object'])
        context['wins'] = context['races'].filter(place=1)
        return context


class HorseDetailView(DetailView):
    model = Horse

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['races'] = Race.objects.filter(crew__horse=context['object'])
        context['wins'] = context['races'].filter(place=1)
        return context
