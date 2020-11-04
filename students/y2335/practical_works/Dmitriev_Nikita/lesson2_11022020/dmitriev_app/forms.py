from django import forms

# import GeeksModel from models.py
from .models import Owner


# create a ModelForm
class OwnerForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Owner
        fields = {
            "firstName",
            "secondName",
            "birthday",
        }
