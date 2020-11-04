from django import forms
from .models import Owner, Car


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = [
            "name",
            "surname",
            "birthday",
        ]


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "manufacturer",
            "model",
            "color",
            "number",
        ]
