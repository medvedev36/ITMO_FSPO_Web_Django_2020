from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class Group_form(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['number_group', 'number_of_student']
        widgets = {
            'number_group': forms.TextInput(attrs={'class': 'form-control'}),
            'number_of_student': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Lecture_form(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['number_lecture', 'number_of_post', 'type']
        widgets = {
            'number_group': forms.TextInput(attrs={'class': 'form-control'}),
            'number_of_student': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'})
        }


class Subject_form(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Teacher_form(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Lesson_form(forms.ModelForm):
    class Meta:
        path = forms.CharField(required=False)
        model = Lesson
        fields = ['number_group', 'number_lecture', 'teacher', 'subject', 'time', 'date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'number_lecture': forms.TextInput(attrs={'class': 'form-control'}),
            'teacher': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
        }
