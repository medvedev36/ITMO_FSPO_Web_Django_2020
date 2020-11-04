from django import forms

from .models import Crew, Horse


class CrewCreateForm(forms.ModelForm):
    class Meta:
        model = Crew
        fields = ['number', 'horse']