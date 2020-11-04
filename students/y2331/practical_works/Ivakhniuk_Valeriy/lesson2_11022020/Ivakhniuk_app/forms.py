from django import forms
from .models import User
from django.views.generic.edit import CreateView
from .models import Auto

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "gender_ch",
            "passport_id",
            "drive_license_id",
            "newrow",
        ]

