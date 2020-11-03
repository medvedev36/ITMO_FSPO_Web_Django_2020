from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class Disk_form(forms.ModelForm):
    class Meta:
        model = Disk
        fields = ['sing', 'production_date', 'price', 'producer']
        widgets = {
            'sing': forms.TextInput(attrs={'class': 'form-control'}),
            'production_date': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'producer': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Sing_form(forms.ModelForm):
    class Meta:
        model = Sing
        fields = ['name', 'singer', 'date', 'type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'singer': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Buy_form(forms.ModelForm):
    class Meta:
        model = Buy
        fields = ['disk']
        widgets = {
            'disk': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Singer_form(forms.ModelForm):
    class Meta:
        model = Singer
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
