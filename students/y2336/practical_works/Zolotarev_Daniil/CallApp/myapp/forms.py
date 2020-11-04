from django import forms
from .models import Account, User
from django.core.exceptions import ValidationError


class AutentificationForm(forms.Form):
    login = forms.SlugField(max_length=20)
    password = forms.CharField(max_length=50)

    login.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})

    def clean_login(self):
        new_login = self.cleaned_data['login'].lower()
        if new_login == 'create':
            raise ValidationError('login may not be "create"')
        return new_login

    def save(self):
        new_account = Account.objects.create(
            login=self.cleaned_data['login'],
            password=self.cleaned_data['password']
        )
        return new_account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['user']
        # widgets = {'user': forms.TextInput(attrs={'class': 'form-control'})}
