from .models import Customers, Registration, Nomer
from django.forms import ModelForm, TextInput
from django import forms


class CustomersForm(ModelForm):
    class Meta:
        model = Customers
        fields = ["fio", "number_phone_cus", "number_passport_customer"]
        widgets = {
            "fio": TextInput(attrs={
                "class": 'form-control',
                "placeholder": 'Зубенко Михаил Петрович'
            }),
            "number_passport_customer": TextInput(attrs={
                "class": 'form-control',
                "placeholder": '402646446'

            }),
            "number_phone_cus": TextInput(attrs={
                "class": 'form-control',
                "placeholder": '89500324063'
            }),
        }


class CustomerFormAuto(ModelForm):
    class Meta:
        model = Customers
        fields = ["number_phone_cus", "number_passport_customer"]
        widgets = {
            "number_phone_cus": TextInput(attrs={
                "class": 'form-control',
                "placeholder": '89500324063'
            }),
            "number_passport_customer": TextInput(attrs={
                "class": 'form-control',
                "placeholder": '402646446',
                "name": 'key_pas'
            }),
        }


class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        nomer = forms.ModelChoiceField(queryset=Nomer.objects.all(), empty_label=None,)
        fields = ["date_entry", "date_exit", "nomer"]
        widgets = {
            "date_entry": TextInput(attrs={
                "class": 'form-control',
                "type": 'date',
                "placeholder": '2020-10-02',
                "name": 'date-entry'
            }),
            "date_exit": TextInput(attrs={
                "class": 'form-control',
                "type": 'date',
                "placeholder": '2020-10-02',
                "name": 'date-exit'
            }),
        }
