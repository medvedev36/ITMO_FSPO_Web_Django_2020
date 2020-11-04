from django import forms
from .models import *


class BoatForm(forms.ModelForm):
    class Meta:
        model = Boat
        fields = [
            "boat_number",
            "mark",
        ]


class OfficerForm(forms.ModelForm):
    class Meta:
        model = Officer
        fields = [
            'badge',
            'surname',
            'post',
            'enrollment',
            'experience',
            'birthday',
            'boat_number'
        ]


class PatrolForm(forms.ModelForm):
    class Meta:
        model = Patrol
        fields = [
            'patrol_id',
            'boat_number',
            'date',
            'district',
            'intruders',
            'reward'
        ]

