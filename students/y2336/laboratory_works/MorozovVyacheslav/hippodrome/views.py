from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CrewCreateForm

# Create your views here.
class CompetitionListView(ListView):
    model = Competition


class CompetitionDetailView(DetailView):
    model = Competition

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['participants'] = Race.objects.filter(competition=context['object']).order_by('place')
        return context


class CompetitionCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Competition
    fields = ['fund', 'name', 'date', 'hippodrome']

    def test_func(self):
        return self.request.user.has_perm('hippodrome.add_compitition')



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


@login_required
def enroll_for_competition(request, competition):
    if request.user in Jockey.objects.filter(crew__race__competition=competition):
        return redirect('competition-detail', competition)
    if request.method == 'POST':
        horse = request.POST.get('horse')
        number = request.POST.get('number')
        crews = Crew.objects.filter(horse_id=horse, jockey=request.user, number=number)
        if crews.count() == 0:
            crew = Crew.objects.create(horse_id=horse, jockey=request.user, number=number)
        else:
            crew = crews.first()
        Race.objects.create(crew=crew, competition_id=competition)
        return redirect('competition-detail', competition)
    else:
        form = CrewCreateForm()
    return render(request, 'hippodrome/race_form.html', {'form': form})