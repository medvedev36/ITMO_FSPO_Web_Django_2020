from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bank.models import *


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["name", "surname", "address", "passport_number",
                  "phone_number", "age", "email"]

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['age'].help_text = 'Укажите свой возрас в формате "2020-08-02"'


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = "__all__"


class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = "__all__"





