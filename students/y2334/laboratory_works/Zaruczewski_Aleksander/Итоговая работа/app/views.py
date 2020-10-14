from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .models import *
from .forms import *


class MyRegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/accounts/login/"

    template_name = "signup.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


def start(request):
    context = {'data_l': Lesson.objects.all(), 'data_t': Teacher.objects.all()}
    return render(request, 'lessons.html', context)


def add_teacher(request):
    context = {}
    form = Teacher_form(request.POST or None)
    context['data_t'] = Teacher.objects.all()
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "add.html", context)


def add_lecture(request):
    context = {}
    form = Lecture_form(request.POST or None)
    context['data_t'] = Lecture.objects.all()
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "add.html", context)


def add_lesson(request):
    context = {}
    form = Lesson_form(request.POST or None)
    context = {'data_les': Lesson.objects.all(), 'data_t': Teacher.objects.all(), 'data_lec': Lecture.objects.all(),
               'data_s': Subject.objects.all(), 'data_g': Group.objects.all()}
    print(form.is_valid())
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "add_lesson.html", context)


def add_group(request):
    context = {}
    form = Group_form(request.POST or None)
    context['data_t'] = Group.objects.all()
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "add.html", context)


def add_subject(request):
    context = {}
    form = Subject_form(request.POST or None)
    context['data_t'] = Subject.objects.all()
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "add.html", context)


def delete_lesson(request, lesson_id):
    try:
        c = Lesson.objects.get(id=lesson_id)
        c.delete()
        return redirect('/base')
    except Lesson.DoesNotExist:
        return HttpResponseNotFound("<h2>Занятие не найдено</h2>")


def logout(request):
    return render(request, "logout.html")
# Create your views here.
