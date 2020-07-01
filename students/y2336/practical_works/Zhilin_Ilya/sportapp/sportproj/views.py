from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from .forms import *
import random


def welcome(request):
    return render(request, "welcome_page.html")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    context = {
        'user': request.user,
    }
    return render(request, 'profile.html', context)


def competition_out(request):
    context = {"competitions": Competition.objects.all()}
    return render(request, "competitions_list.html", context)


class competition_in(View):
    def get(self, request):
        form = CompetitionForm()
        return render(request, 'competitions_form.html', context={'form': form})

    def post(self, request):
        new_comp = CompetitionForm(request.POST).save()
        return redirect('competitions_form')


def trainer_out(request):
    context = {"trainers": Trainer.objects.all()}
    return render(request, "trainers_list.html", context)


class trainer_in(View):
    def get(self, request):
        form = TrainerForm()
        return render(request, 'trainers_form.html', context={'form': form})

    def post(self, request):
        new_trainer = TrainerForm(request.POST).save()
        return redirect('trainers_form')


def sportsman_out(request):
    context = {"sportsmen": Sportsman.objects.all()}
    return render(request, "sportsmen_list.html", context)


class sportsman_in(View):
    def get(self, request):
        form = SportsmanForm()
        return render(request, 'sportsmen_form.html', context={'form': form})

    def post(self, request):
        new_sport = SportsmanForm(request.POST).save()
        return redirect('sportsmen_form')


def trauma_out(request):
    context = {"traumas": Trauma.objects.all()}
    return render(request, "traumas_list.html", context)


class trauma_in(View):
    def get(self, request):
        form = TraumaForm
        return render(request, 'traumas_form.html', context={'form': form})

    def post(self, request):
        new_trauma = TraumaForm(request.POST).save()
        return redirect('traumas_form')


def contest_out(request):
    context = {"contest": Contest.objects.all()}
    return render(request, "contest_list.html", context)


class contest_in(View):
    def get(self, request):
        form = ContestForm
        return render(request, 'contest_form.html', context={'form': form})

    def post(self, request):
        new_contest = ContestForm(request.POST).save()
        return redirect('contest_form')


def binding(request):
    context = {}
    cur_user = request.user
    if request.method == 'POST':
        user = User.objects.get(username=cur_user)
        form = AccountForm(request.POST, instance=user)
        qwerty = request.POST.get('sportsman')
        print(qwerty)
        if form.is_valid():
            form.save()
        context = {'form': form}
    else:
        form = AccountForm()
        context = {'form': form}
    return render(request, 'binding.html', context)


def participation(request):
    cur_user = request.user
    if request.method == 'POST':
        user = User.objects.get(username=cur_user)
        sportsman = Sportsman.objects.get(name=user.sportsman.name)
        trainer = sportsman.trainer
        com = request.POST.get('competition')
        com = Competition.objects.get(title=com)
        pos = random.randint(1, 25)
        Contest.objects.create(competition=com, sportsman=sportsman, trainer=trainer,
                               sportsman_position=pos, sportsman_score=50//pos, trainer_score=50//pos)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'participation.html')


def workout_out(request):
    context = {"workout": Workout.objects.all()}
    return render(request, "workout_list.html", context)


def training(request):
    cur_user = request.user
    if request.method == 'POST':
        user = User.objects.get(username=cur_user)
        sportsman = user.sportsman
        trainer = request.POST.get('trainer')
        trainer = Trainer.objects.get(name=trainer)
        string_date = request.POST.get('date')
        Workout.objects.create(sportsman=sportsman, trainer=trainer, date=string_date)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'training.html')
