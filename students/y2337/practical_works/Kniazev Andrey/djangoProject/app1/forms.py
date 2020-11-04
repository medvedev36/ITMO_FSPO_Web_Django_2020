from django import forms
from .models import *


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = [
            "first_name",
            "last_name",
            "birthdate",
            "user",
        ]


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "model",
            "color",
            "number",
        ]

