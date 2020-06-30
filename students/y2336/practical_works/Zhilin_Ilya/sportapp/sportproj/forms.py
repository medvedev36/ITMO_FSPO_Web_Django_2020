from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['sportsman']


class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ["title", "date", "place", "category"]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "date": forms.DateInput(attrs={'class': 'form-control'}),
            "place": forms.TextInput(attrs={'class': 'form-control'}),
            "category": forms.NumberInput(attrs={'class': 'form-control'}),
        }


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ["name", "phone", "category", "rating", "salary"]
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "phone": forms.NumberInput(attrs={'class': 'form-control'}),
            "category": forms.NumberInput(attrs={'class': 'form-control'}),
            "rating": forms.NumberInput(attrs={'class': 'form-control'}),
            "salary": forms.NumberInput(attrs={'class': 'form-control'}),
        }


class SportsmanForm(forms.ModelForm):
    class Meta:
        model = Sportsman
        fields = ["name", "category", "age", "rating", "trainer"]
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "category": forms.NumberInput(attrs={'class': 'form-control'}),
            "age": forms.NumberInput(attrs={'class': 'form-control'}),
            "rating": forms.NumberInput(attrs={'class': 'form-control'}),
            "trainer": forms.RadioSelect(attrs={'class': 'form-control'}),
        }


class TraumaForm(forms.ModelForm):
    class Meta:
        model = Trauma
        fields = ["sportsman", "type"]
        widgets = {
            "sportsman": forms.RadioSelect(attrs={'class': 'form-control'}),
            "type": forms.TextInput(attrs={'class': 'form-control'}),
        }


class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ["competition", "sportsman", "trainer", "sportsman_position", "sportsman_score", "trainer_score"]
        widgets = {
            "competition": forms.RadioSelect(attrs={'class': 'form-control'}),
            "sportsman": forms.RadioSelect(attrs={'class': 'form-control'}),
            "trainer": forms.RadioSelect(attrs={'class': 'form-control'}),
            "sportsman_position": forms.NumberInput(attrs={'class': 'form-control'}),
            "sportsman_score": forms.NumberInput(attrs={'class': 'form-control'}),
            "trainer_score": forms.NumberInput(attrs={'class': 'form-control'}),
        }
