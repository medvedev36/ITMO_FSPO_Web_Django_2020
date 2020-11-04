from django import forms
from .models import Owner, Auto


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner

        fields = ["usr", "first_name", "last_name", "birthday"]


