from django import forms
from .models import *


class VoyageForm(forms.ModelForm):
    class Meta:
        model = Voyage
        fields = [
            "voyage_id",
            "trawler_id",
            "start_date",
            "end_date",
            "bank_name",
            "fish_name",
            "fish_quantity"
        ]


class TrawlerForm(forms.ModelForm):
    class Meta:
        model = Trawler
        fields = [
            'trawler_id',
            'tname',
            'displacement',
            'prod_date'
        ]


class CrewForm(forms.ModelForm):
    class Meta:
        model = Crew
        fields = [
            'member_id',
            'trawler_id',
            'member_name',
            'member_job',
            'hire_date',
            'bday',
            'to_pension'
        ]

