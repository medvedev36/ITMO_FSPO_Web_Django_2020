from django import forms

from .models import FuelInStation


class FuelInStationForm(forms.ModelForm):

    class Meta:
        model = FuelInStation
        fields = ['price', 'fuel']