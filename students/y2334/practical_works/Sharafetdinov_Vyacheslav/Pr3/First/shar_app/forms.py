from django import forms
from .models import Owner, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class User_CreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'nationality', 'address')

class User_ChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'nationality', 'address')

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = [
            "user",
            "first_name",
            "second_name",
            "sex",
            "passport",
        ]