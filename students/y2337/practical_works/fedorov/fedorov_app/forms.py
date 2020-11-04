from django import forms
from .models import *


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = [
            "second_name",
            "first_name",
            "birthday",
            "sex"
        ]


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "id",
            "model",
            "provider"
        ]
