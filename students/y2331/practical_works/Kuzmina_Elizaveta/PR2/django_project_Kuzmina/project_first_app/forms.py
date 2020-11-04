from django import forms
from .models import CarOwner


class OwnersForm(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = "__all__"
