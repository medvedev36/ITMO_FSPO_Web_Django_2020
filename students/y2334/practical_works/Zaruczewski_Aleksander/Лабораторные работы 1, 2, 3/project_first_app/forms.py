from django import forms
from project_first_app.models import *


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner

        fields = [
            "first_name",
            "last_name",
            "birth_date",
            "sex",
            "user",
        ]