from .models import Owner
from django import forms

class OwnerForm(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = Owner

        # specify fields to be used
        fields = [
            "user",
            "firstName",
            "secondName",
        ]