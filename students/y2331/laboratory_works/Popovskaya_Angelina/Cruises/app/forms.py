from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from un import settings
from .models import *


class Selling_form(forms.ModelForm):
    class Meta:
        model = Sell
        fields = ['id_excursion', 'id_profile', 'price']
        widgets = {
            'id_excursion': forms.TextInput(attrs={'class': 'form-control'}),
            'id_profile': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SignUpForm(UserCreationForm):
    photo = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'photo', 'password1', 'password2')


class Excursions_form(forms.ModelForm):

    class Meta:
        model = Excursion
        fields = ['id_cruise', 'date_of_departure', 'date_of_arrival', 'quantity_post_of_1', 'quantity_post_of_2', 'quantity_post_of_3', 'information', 'photo']
        widgets = {
            'id_cruise': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_departure': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_arrival': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity_post_of_1': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity_post_of_2': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity_post_of_3': forms.TextInput(attrs={'class': 'form-control'}),
            'information': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Cruise_form(forms.ModelForm):

    class Meta:
        model = Cruise
        fields = ['name', 'reg_number', 'price_1', 'price_2', 'price_3', 'name_captain']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'reg_number': forms.TextInput(attrs={'class': 'form-control'}),
            'price_1': forms.TextInput(attrs={'class': 'form-control'}),
            'price_2': forms.TextInput(attrs={'class': 'form-control'}),
            'price_3': forms.TextInput(attrs={'class': 'form-control'}),
            'name_captain': forms.TextInput(attrs={'class': 'form-control'}),
        }