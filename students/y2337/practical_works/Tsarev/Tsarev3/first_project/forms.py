from django import forms
from .models import Owner, Auto


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = [
            "first_name",
            "last_name",
            "birthday",
        ]


class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = [
            "auto_id",
            "model",
            "color",
            "license_plate",
        ]
