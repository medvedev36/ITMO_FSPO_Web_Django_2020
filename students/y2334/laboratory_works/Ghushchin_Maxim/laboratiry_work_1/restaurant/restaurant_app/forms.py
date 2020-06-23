from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from restaurant_app.models import *


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['phone']

