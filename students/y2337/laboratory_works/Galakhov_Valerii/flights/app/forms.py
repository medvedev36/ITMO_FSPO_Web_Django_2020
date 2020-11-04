from django import forms
from .models import *


class HelicopterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dateOfProduction'].label = "Дата производства"

    dateOfProduction = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Helicopter
        fields = [
            "name",
            "carryingCapacity",
            "dateOfProduction",
        ]


class PilotForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dateOfBirth'].label = "Дата рождения"

    dateOfBirth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Pilot
        fields = [
            "idHelicopter",
            "pilotName",
            "pilotPost",
            "pilotExperience",
            "dateOfBirth",
        ]


class FlightForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dateOfFlight'].label = "Дата рейса"

    dateOfFlight = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Flight
        fields = [
            "idHelicopter",
            "dateOfFlight",
            "cargoWeight",
            "flightDuration",
            "flightCost",
        ]


